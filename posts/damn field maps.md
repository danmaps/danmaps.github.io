---
date: 2024-08-21
tags:
- python
- gis
- arcgis
title: Field Mapping Frustrations in GIS - Automating Spatial Joins
---

Last week, I ran into an issue with a batch spatial join tool that ran smoothly on several feature classes, each with slightly different schemas. However, without any warning, the tool produced outputs with a bunch of null values. If you’ve ever worked with field mapping in GIS, you might be familiar with this problem. I wanted to write about my experience and the solution I found, so I don’t forget it in the future.

Here’s an example of the tool setup:

```python
arcpy.ImportToolbox(r"C:\Temp\MyToolbox.atbx")
arcpy.MyToolbox.BatchSpatialJoin(
    target_features=r"Data\City_Parcels.shp",
    join_features=r"Data\Park_Boundaries.shp",
    out_feature_class=r"Output\Parcels_With_Parks.gdb\Parcels_Parks_Join",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping=r'PARCEL_ID "PARCEL_ID" true true false 8 Long 0 0,First,#,City_Parcels,PARCEL_ID,-1,-1;PARK_NAME "PARK_NAME" true true false 255 Text 0 0,First,#,Park_Boundaries,PARK_NAME,0,254',
    match_option="INTERSECT"
)
```

Notice that **field_mapping**—it looks complicated! The issue here is that the field mapping won’t work well when there are differences in field names or schemas between datasets. When running a tool manually, this mapping is handled during parameter validation. However, when automating via Python or ModelBuilder, it silently fails, resulting in null values.

At first, I tried editing the field mapping string manually, but that process turned out to be error-prone and tedious. After some trial and error, I created a function to automate the process of generating field mappings in a more reliable way.

Here’s the function that helped:

```python
def create_field_mappings(target, join, join_field, output_field_name=None, merge_rule=None, delimiter=', ', output_field_length=255):
    """
    Creates field mappings for spatial join, setting output field as text type and specified length.

    Parameters:
    target (str): The target feature class for the join.
    join (str): The join feature class.
    join_field (str): The field name in the join feature class to match properties.
    output_field_name (str, optional): The name for the output field. Default is the same as join_field.
    merge_rule (str, optional): The merge rule to apply ('Join', 'Sum', 'Mean', etc.). Default is None.
    delimiter (str, optional): The delimiter for 'Join' merge rule. Default is ', '.
    output_field_length (int, optional): The length for the output field. Default is 255.

    Returns:
    arcpy.FieldMappings: The field mappings for the spatial join.
    """
    # Create field mappings
    field_mappings = arcpy.FieldMappings()
    field_mappings.addTable(target)

    # Create and set up the field map
    field_map = arcpy.FieldMap()
    field_map.addInputField(join, join_field)

    # Set output field properties
    out_field = arcpy.Field()
    out_field.name = output_field_name if output_field_name else join_field
    out_field.aliasName = out_field.name
    if merge_rule:
        field_map.mergeRule = merge_rule
        if merge_rule.lower() == 'join':
            field_map.joinDelimiter = delimiter

    field_map.outputField = out_field

    # Add the field map to the field mappings
    field_mappings.addFieldMap(field_map)

    return field_mappings
```

This function effectively recreates the field mapping behavior you'd expect when running the tool manually, but with more control and automation. Using it saved me time and eliminated the frustration of manually editing long field mapping strings.

The key takeaway: when working with batch processes or automated tools in GIS, don’t rely on silent errors to reveal themselves later—create automated solutions for common pitfalls like field mappings. It’s worth the effort!
