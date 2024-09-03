---
date: 2024-08-21
tags:
- Python
- GIS
- ArcGIS Pro
title: Damn field mappings!
---


Today, I created a batch spatial join tool and it happily ran on three different feature classes with slightly different schemas. without warning, it created null values in the output.

I have to remember this going forward, so i'm writing about it.

```python 
arcpy.ImportToolbox(r"C:\Users\mcveydb\AppData\Local\Temp\ArcGISProTemp33628\Tmp.atbx")
arcpy.Tmp.BatchSpatialJoin(
    target_features=r"AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans",
    join_features=r"\\sce\workgroup\CRE3\SMG\PROJECTS\Special_Projects\2020_Emergent_Dry_ Fuel_Work\2024\AOC_Fall_2024\AOC_2024_Fall.shp",
    out_feature_class=r"\\sce\workgroup\CRE3\SMG\PROJECTS\Special_Projects\2020_Emergent_Dry_ Fuel_Work\2024\AOC_Fall_2024\AOC_Fall_2024.gdb\%Name%_join",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping=r'GESW_GESW_ID "GESW_GESW_ID" true true false 8 Double 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,GESW_GESW_ID,-1,-1;M3D_SCE_FID_GESW_COND "M3D_SCE_FID_GESW_COND" true true false 8 Double 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,M3D_SCE_FID_GESW_COND,-1,-1;CDS_CIRCUIT_NAME "CDS_CIRCUIT_NAME" true true false 150 Text 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,CDS_CIRCUIT_NAME,0,149;CDS_CIRCUIT_CONCAT "CDS_CIRCUIT_CONCAT" true true false 251 Text 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,CDS_CIRCUIT_CONCAT,0,250;M3D_SCE_ID_OH_UG_VAL "M3D_SCE_ID_OH_UG_VAL" true true false 255 Text 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,M3D_SCE_ID_OH_UG_VAL,0,254;M3D_ID_CONDUCTOR_TYPE_VAL "M3D_ID_CONDUCTOR_TYPE_VAL" true true false 255 Text 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,M3D_ID_CONDUCTOR_TYPE_VAL,0,254;M3D_ID_VOLTAGE_VAL "M3D_ID_VOLTAGE_VAL" true true false 255 Text 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,M3D_ID_VOLTAGE_VAL,0,254;M3D_SCE_ID_NO_OF_WIRES_VAL "M3D_SCE_ID_NO_OF_WIRES_VAL" true true false 255 Text 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,M3D_SCE_ID_NO_OF_WIRES_VAL,0,254;CDS_ANNOTATION_TEXT "CDS_ANNOTATION_TEXT" true true false 2000 Text 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,CDS_ANNOTATION_TEXT,0,1999;StaticObjID "StaticObjID" true true false 4 Long 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,StaticObjID,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,AOC_2024_FALL_TRANS\AOC_2024_Fall_Trans,Shape_Length,-1,-1;OBJECTID "OBJECTID" true true false 10 Long 0 10,First,#,\\sce\workgroup\CRE3\SMG\PROJECTS\Special_Projects\2020_Emergent_Dry_ Fuel_Work\2024\AOC_Fall_2024\AOC_2024_Fall.shp,OBJECTID,-1,-1;Area_Name "Area_Name" true true false 100 Text 0 0,First,#,\\sce\workgroup\CRE3\SMG\PROJECTS\Special_Projects\2020_Emergent_Dry_ Fuel_Work\2024\AOC_Fall_2024\AOC_2024_Fall.shp,Area_Name,0,99;Tier "Tier" true true false 50 Text 0 0,First,#,\\sce\workgroup\CRE3\SMG\PROJECTS\Special_Projects\2020_Emergent_Dry_ Fuel_Work\2024\AOC_Fall_2024\AOC_2024_Fall.shp,Tier,0,49;FCZ "FCZ" true true false 50 Text 0 0,First,#,\\sce\workgroup\CRE3\SMG\PROJECTS\Special_Projects\2020_Emergent_Dry_ Fuel_Work\2024\AOC_Fall_2024\AOC_2024_Fall.shp,FCZ,0,49',
    match_option="INTERSECT",
    search_radius=None,
    distance_field_name="",
    match_fields=None
)
```

Look at that field_mapping, what a mess! It won't work at all for datasets with different names, let alone different fields. When running the tool manually over and over again, the field mapping parameter is set during parameter validation based on the value of the "target_features". 

When running in batch mode or automated with python or model builder, there isn't an error produced. It might just run and create a bunch of null values in the output.

Does this happen with other methods? Like tabular joins, or similiar joins in pandas or geopandas? To be explored.

At first I tried to manually edit the field_mapping string itself, but that proved to be a fragile annoying process. I'm automating to avoid error prone tedium, not increase it!

Throught trial and error, i was able to make this work using the following function:
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
    if output_field_name == 'COUNTY':
        out_field.type = "String"  # Explicitly set as text type
        out_field.length = output_field_length  # Set length to 255

    if merge_rule:
        field_map.mergeRule = merge_rule
        if merge_rule.lower() == 'join':
            field_map.joinDelimiter = delimiter

    field_map.outputField = out_field

    # Add the field map to the field mappings
    field_mappings.addFieldMap(field_map)

    return field_mappings
```

The goal was to recreated, effectively, the field_mapping creation that happens when running the tool manually, but in a different context. It works!