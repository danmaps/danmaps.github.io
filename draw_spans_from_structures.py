import arcpy
import os
import math

def draw_spans_from_structures(structures_fc, output_spans_fc):
    arcpy.env.overwriteOutput = True

    # Step 1: Build lookup: pole_id -> geometry
    pole_geometries = {}
    with arcpy.da.SearchCursor(structures_fc, ["pole_id", "SHAPE@XY"]) as cursor:
        for pole_id, xy in cursor:
            pole_geometries[pole_id] = xy

    # Step 2: Create span features: from each pole to its next_id
    span_features = []
    with arcpy.da.SearchCursor(structures_fc, ["pole_id", "next_id"]) as cursor:
        for pole_id, next_id in cursor:
            if not next_id:
                continue  # Skip if no next_id
            start_xy = pole_geometries.get(pole_id)
            end_xy = pole_geometries.get(next_id)
            if start_xy and end_xy:
                array = arcpy.Array([
                    arcpy.Point(*start_xy),
                    arcpy.Point(*end_xy)
                ])
                line = arcpy.Polyline(array)
                span_features.append((pole_id, next_id, line))

    # Step 3: Create output feature class
    workspace = os.path.dirname(output_spans_fc)
    if not arcpy.Exists(workspace):
        arcpy.management.CreateFeatureDataset(os.path.dirname(workspace), os.path.basename(workspace))
    spatial_ref = arcpy.Describe(structures_fc).spatialReference
    arcpy.management.CreateFeatureclass(
        out_path=workspace,
        out_name=os.path.basename(output_spans_fc),
        geometry_type="POLYLINE",
        spatial_reference=spatial_ref
    )

    # Step 4: Add fields
    arcpy.management.AddField(output_spans_fc, "from_id", "TEXT", field_length=50)
    arcpy.management.AddField(output_spans_fc, "to_id", "TEXT", field_length=50)
    arcpy.management.AddField(output_spans_fc, "bearing_quadrant", "TEXT", field_length=20)

    # Step 5: Insert spans (from_id, to_id, geometry)
    with arcpy.da.InsertCursor(output_spans_fc, ["from_id", "to_id", "SHAPE@"]) as cursor:
        for from_id, to_id, shape in span_features:
            cursor.insertRow((from_id, to_id, shape))

    # Step 6: Add Geometry Attributes: Length + Line Bearing (azimuth degrees)
    arcpy.management.AddGeometryAttributes(
        Input_Features=output_spans_fc,
        Geometry_Properties="LENGTH;LINE_BEARING",
        Length_Unit="FOOT_US"
    )

    # Step 7: Update quadrant-style bearing
    with arcpy.da.UpdateCursor(output_spans_fc, ["Bearing", "bearing_quadrant"]) as cursor:
        for row in cursor:
            azimuth = row[0]
            if azimuth is not None:
                quadrant_bearing = degrees_to_quadrant_bearing(azimuth)
                row[1] = quadrant_bearing
                cursor.updateRow(row)

    print(f"Created {len(span_features)} spans with Length (ft), Azimuth (deg), and Quadrant Bearing in {output_spans_fc}")

def degrees_to_quadrant_bearing(angle_deg):
    """
    Convert azimuth degrees (0-360) to compass quadrant bearing (like N45E).
    """
    if angle_deg >= 0 and angle_deg < 90:
        return f"N{round(angle_deg)}E"
    elif angle_deg >= 90 and angle_deg < 180:
        return f"S{round(180 - angle_deg)}E"
    elif angle_deg >= 180 and angle_deg < 270:
        return f"S{round(angle_deg - 180)}W"
    else:
        return f"N{round(360 - angle_deg)}W"

# Example usage:
# draw_spans_from_structures("Structures_With_Next", "Spans_From_Structures")
