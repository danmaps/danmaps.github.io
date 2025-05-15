from arcgis.gis import GIS
from arcgis.features import FeatureLayer

# Connect to GIS (use Pro context)
gis = GIS("pro")  # This uses your signed-in Pro session

# Feature layer URL
layer_url = "https://services6.arcgis.com/sIGsGHq6XlKtUAL8/arcgis/rest/services/CA_LB_PRO/FeatureServer/3"

# Access the layer
layer = FeatureLayer(layer_url, gis=gis)

# Define query parameters safely
where_clause = "1=1"
geometry = {
    "xmin": -13417214.5529552419,
    "ymin": 3919744.3389966148,
    "xmax": -12705061.7473576926,
    "ymax": 4636886.3236006815,
    "spatialReference": {"wkid": 102100}
}

# Safe paginated query using POST under the hood
result = layer.query(
    where=where_clause,
    geometry=geometry,
    geometry_type='esriGeometryEnvelope',
    spatial_rel='esriSpatialRelIntersects',
    out_fields="OBJECTID",
    return_geometry=True,
    result_offset=16000,
    result_record_count=4000,
    out_sr=102100,
    return_true_curves=True,
    return_pbf=True  # Automatically uses POST if needed
)

print(f"Returned {len(result.features)} features.")

'''
| Feature                        | Why it's safe in ArcGIS Pro                                          |
| ------------------------------ | -------------------------------------------------------------------- |
| Uses `FeatureLayer.query()`    | Handles method (`GET` vs `POST`) automatically based on payload size |
| Uses `return_pbf=True`         | Returns compressed protobuf geometry, but still safe via API         |
| Uses `gis = GIS("pro")`        | Uses the logged-in Pro session, so **no token issues**               |
| **No manual URL construction** | Avoids `ERROR 003986` due to bad URL encoding                        |

'''