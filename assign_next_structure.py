import arcpy
import os

def assign_next_structure_with_m(points_fc, line_fc, output_fc):
    arcpy.env.overwriteOutput = True
    gdb = arcpy.env.scratchGDB

    # Step 1: Create a Route from the circuit line
    route_fc = os.path.join(gdb, "circuit_route")
    arcpy.lr.CreateRoutes(
        in_line_features=line_fc,
        route_id_field="OBJECTID",  # assuming one line or unique ID
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

    # Step 4: Build sorted list by LINE_M (M-value)
    poles = []
    with arcpy.da.SearchCursor(output_fc, ["OID@", "pole_id", "LINE_M"]) as cursor:
        for oid, pid, m in cursor:
            if m is not None:
                poles.append((oid, pid, m))

    poles.sort(key=lambda x: x[2])  # Sort by M-value increasing

    # Step 5: Prepare next_id and distance_to_next mapping
    oid_to_next_info = {
        poles[i][0]: (poles[i+1][1], poles[i+1][2] - poles[i][2])
        for i in range(len(poles) - 1)
    }

    # Step 6: Update next_id and distance_to_next fields
    with arcpy.da.UpdateCursor(output_fc, ["OID@", "next_id", "distance_to_next"]) as cursor:
        for row in cursor:
            oid = row[0]
            if oid in oid_to_next_info:
                next_id, dist = oid_to_next_info[oid]
                row[1] = next_id
                row[2] = dist
                cursor.updateRow(row)

    print(f"Assigned next_id and distance_to_next for {len(oid_to_next_info)} structures.")

# Example usage:
# assign_next_structure_with_m("Structures", "CircuitLine", "Structures_With_Next")
