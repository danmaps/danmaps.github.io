import arcpy
import os

def assign_next_structure(points_fc, line_fc, output_fc):
    arcpy.env.overwriteOutput = True

    # 1. Copy points_fc to output_fc so we can edit it
    arcpy.management.CopyFeatures(points_fc, output_fc)

    # 2. Add fields: projected_measure and next_id
    if not [f.name for f in arcpy.ListFields(output_fc) if f.name.lower() == "proj_m"]:
        arcpy.management.AddField(output_fc, "proj_m", "DOUBLE")
    if not [f.name for f in arcpy.ListFields(output_fc) if f.name.lower() == "next_id"]:
        arcpy.management.AddField(output_fc, "next_id", "TEXT", field_length=50)

    # 3. Create near table with location along the line
    near_table = os.path.join(arcpy.env.scratchGDB, "near_table")
    arcpy.analysis.GenerateNearTable(
        in_features=output_fc,
        near_features=line_fc,
        out_table=near_table,
        search_radius="100 Meters",
        location="LOCATION",
        angle="NO_ANGLE",
        closest="CLOSEST",
        closest_count=1
    )

    # 4. Read projected points with measure along the line
    oid_to_measure = {}
    with arcpy.da.SearchCursor(near_table, ["IN_FID", "NEAR_DIST", "NEAR_X", "NEAR_Y"]) as cursor:
        for oid, near_dist, near_x, near_y in cursor:
            # For now, store NEAR_X as a proxy for along-line location (approximate)
            oid_to_measure[oid] = (near_x, near_y)

    # 5. Write proj_m values into points
    with arcpy.da.UpdateCursor(output_fc, ["OID@", "proj_m"]) as cursor:
        for oid, proj_m in cursor:
            if oid in oid_to_measure:
                near_x, near_y = oid_to_measure[oid]
                cursor.updateRow((oid, near_x))  # using NEAR_X for now; could use smarter linear referencing if available

    # 6. Build list of structures ordered by proj_m
    ordered_poles = []
    with arcpy.da.SearchCursor(output_fc, ["OID@", "proj_m"]) as cursor:
        for oid, proj_m in cursor:
            if proj_m is not None:
                ordered_poles.append((oid, proj_m))
    ordered_poles.sort(key=lambda x: x[1])  # Sort by measure

    # 7. Assign next_id
    oid_to_next = {ordered_poles[i][0]: ordered_poles[i+1][0] for i in range(len(ordered_poles)-1)}

    with arcpy.da.UpdateCursor(output_fc, ["OID@", "next_id"]) as cursor:
        for oid, next_id in cursor:
            if oid in oid_to_next:
                cursor.updateRow((oid, str(oid_to_next[oid])))

    print(f"Assigned next_id for {len(oid_to_next)} structures.")

# Example usage:
# assign_next_structure("Structures", "CircuitLine", "Structures_With_Next")
