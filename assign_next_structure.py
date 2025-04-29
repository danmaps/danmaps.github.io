import arcpy
import os

def assign_next_structure_with_m(points_fc, line_fc, output_fc):
    arcpy.env.overwriteOutput = True
    gdb = arcpy.env.scratchGDB

    # Step 1: Create a Route from the circuit line
    route_fc = os.path.join(gdb, "circuit_route")
    arcpy.lr.CreateRoutes(
        in_line_features=line_fc,
        route_id_field="OBJECTID",
        out_feature_class=route_fc,
        measure_source="LENGTH"
    )

    # Step 2: Locate structures along the route
    located_fc = os.path.join(gdb, "located_points")
    arcpy.lr.LocateFeaturesAlongRoutes(
        in_features=points_fc,
        in_routes=route_fc,
        route_id_field="OBJECTID",
        out_table=located_fc,
        search_radius="50 Meters",
        distance_field="MEAS_DIST",
        route_location_fields="ROUTE_ID LINE_M"
    )

    # Step 3: Copy located points to output and add fields
    arcpy.management.CopyFeatures(located_fc, output_fc)

    existing_fields = [f.name.lower() for f in arcpy.ListFields(output_fc)]

    if "next_id" not in existing_fields:
        arcpy.management.AddField(output_fc, "next_id", "TEXT", field_length=50)
    if "distance_to_next" not in existing_fields:
        arcpy.management.AddField(output_fc, "distance_to_next", "DOUBLE")

    # Step 4: Build sorted list by LINE_M
    poles = []
    with arcpy.da.SearchCursor(output_fc, ["OID@", "pole_id", "LINE_M"]) as cursor:
        for oid, pid, m in cursor:
            if m is not None:
                poles.append((oid, pid, m))

    poles.sort(key=lambda x: x[2])  # Sort by M-value

    # Step 5: Assign next_id
    oid_to_next_oid = {poles[i][0]: poles[i+1][0] for i in range(len(poles) - 1)}

    # Step 6: Generate Near Table for accurate distance
    near_table = os.path.join(gdb, "near_table")

    # Create a temporary layer to restrict near search to next points only
    oid_to_next_oid_list = [(oid, next_oid) for oid, next_oid in oid_to_next_oid.items()]
    oid_mapping_table = os.path.join(gdb, "oid_mapping")
    arcpy.da.NumPyArrayToTable(
        arcpy.da.NumPyArrayFromRecords(oid_to_next_oid_list, ["IN_FID", "NEAR_FID"]),
        oid_mapping_table
    )

    # Spatial join the source points to themselves using custom matches
    arcpy.analysis.GenerateNearTable(
        in_features=output_fc,
        near_features=output_fc,
        out_table=near_table,
        search_radius=None,
        location="NO_LOCATION",
        angle="NO_ANGLE",
        closest="ALL",
        closest_count=1
    )

    # Step 7: Build accurate distance lookup
    distance_lookup = {}
    with arcpy.da.SearchCursor(near_table, ["IN_FID", "NEAR_FID", "NEAR_DIST"]) as cursor:
        for in_fid, near_fid, near_dist in cursor:
            if oid_to_next_oid.get(in_fid) == near_fid:
                distance_lookup[in_fid] = near_dist

    # Step 8: Update next_id and distance_to_next in output_fc
    with arcpy.da.UpdateCursor(output_fc, ["OID@", "next_id", "distance_to_next", "pole_id"]) as cursor:
        for row in cursor:
            oid = row[0]
            if oid in oid_to_next_oid:
                next_oid = oid_to_next_oid[oid]
                # Need to get the next pole_id
                next_pid = None
                for p in poles:
                    if p[0] == next_oid:
                        next_pid = p[1]
                        break
                row[1] = next_pid
                row[2] = distance_lookup.get(oid)
                cursor.updateRow(row)

    print(f"Assigned next_id and near-table-based distance_to_next for {len(oid_to_next_oid)} structures.")
