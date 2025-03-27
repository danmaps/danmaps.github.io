---
date: 2024-08-13
tags:
- gis
- python
- open-source

title: Open source alternatives to ArcPy
---

**"The best camera is the one you have with you."**

You'd be surprised --- if you're like me --- at the ease and availability of alternatives to ArcPy. Just like the camera analogy above, the best geoprocessing tools are the ones you have with you. In my line of work, that's usually ArcPy. We've all got ArcGIS Pro installed locally, so we can do whatever we want.

But what if we want to get something done elsewhere? Like using Streamlit for web apps or running scripts on a server where ArcGIS Pro isn't installed? It turns out there are numerous capable alternatives to ArcPy, especially when you consider that the majority of our geoprocessing operations fall into the "bread and butter" category. I’m talking about tasks like tabular joins, spatial joins, buffering, and other routine operations. You can get relatively simple tasks like this done using open-source Python libraries like GeoPandas, Shapely, and Fiona. These tools are all free to use, easy to install, and very intuitive. They even work with projected coordinate systems, so you can trust the accuracy of your results.

In this post, we'll discuss how to run these tools, how they compare to ArcPy, and how you can assess the accuracy of the results to ensure you're getting what you expect.

## Running Geoprocessing Tools in ArcGIS Pro

ArcGIS Pro, with its ArcPy library, is a powerful tool for geospatial analysis. ArcPy comes bundled with a wide range of geoprocessing functions that make spatial data manipulation easy. For example, if you need to perform a spatial join, buffer some points, or clip a dataset, ArcPy provides straightforward functions to do this:

```python
import arcpy

# Example of buffering points
input_points = "points.shp"
output_buffer = "buffered_points.shp"
buffer_distance = "100 Meters"

arcpy.Buffer_analysis(input_points, output_buffer, buffer_distance)
```

This kind of operation is standard in GIS workflows and can be executed efficiently within ArcGIS Pro. The tools are designed to work with a wide range of spatial data formats, projections, and coordinate systems, which adds to their robustness.

However, ArcGIS Pro is a heavyweight application, and ArcPy scripts are typically tied to an ArcGIS Pro installation. This means you need access to a licensed copy of ArcGIS Pro to use ArcPy, which might not be feasible in all scenarios—especially if you're working in a more lightweight or cloud-based environment.

## Using Open Source Python Libraries Outside of ArcGIS Pro

If you find yourself in a situation where ArcGIS Pro isn’t available, or you simply want to explore more lightweight, open-source options, Python's geospatial libraries have you covered.

### GeoPandas

GeoPandas is a popular open-source library that extends Pandas to allow spatial operations on geometric types. It simplifies the process of reading, writing, and manipulating spatial data in Python. Here's an example of performing a buffer operation using GeoPandas:

```python
import geopandas as gpd

# Read the shapefile
points = gpd.read_file("points.shp")

# Buffer the points by 100 meters
buffered_points = points.buffer(100)

# Save the result
buffered_points.to_file("buffered_points.shp")
```

GeoPandas supports a wide range of spatial operations, including joins, dissolves, and overlays, making it a viable alternative for many standard geoprocessing tasks.

### Shapely and Fiona

For more granular control, you can combine Shapely and Fiona. Shapely handles geometric operations, while Fiona reads and writes vector data. This approach gives you a more modular and flexible setup, though it requires a bit more coding:

```python
from shapely.geometry import Point
from fiona import collection

# Create a point and buffer it
point = Point(1, 1)
buffered = point.buffer(100)

# Save to a shapefile
schema = {'geometry': 'Polygon', 'properties': {}}
with collection("buffered_point.shp", "w", "ESRI Shapefile", schema) as output:
    output.write({'geometry': buffered.wkt, 'properties': {}})
```

These tools allow for more customizable workflows and can be integrated into a variety of applications, including web apps, server-side processing, and batch jobs on remote servers.

## Comparing Results

When using different tools for the same tasks, it's crucial to ensure that the results are consistent and accurate. A common approach is to perform the same operation in both ArcPy and an open-source library, then compare the outputs.

For example, after buffering points in both ArcPy and GeoPandas, you can compare the results by checking the area of the resulting polygons or by overlaying the outputs in a GIS application and visually inspecting them.

```python
# Example comparison of buffer areas
arcpy_area = arcpy.Describe("buffered_points.shp").area
gpd_area = buffered_points.geometry.area.sum()

print(f"ArcPy area: {arcpy_area}, GeoPandas area: {gpd_area}")
```

You can also use specific metrics like intersection over union (IoU) for spatial comparisons, or you can check the attribute tables to ensure the same features were retained or joined correctly. This helps ensure that the results are consistent and accurate. Over time, your confidence in the results will increase, but it's still important to use common sense to evaluate the quality of outputs.

## Conclusion

ArcPy is a powerful tool, and for many GIS professionals, it’s the default option for spatial analysis. However, as we've seen, there are robust open-source alternatives that can handle many of the same tasks, often with fewer dependencies and more flexibility in terms of deployment.

Whether you're looking to build lightweight web apps, run scripts on a server, or just explore what’s possible outside of ArcGIS Pro, tools like GeoPandas, Shapely, and Fiona offer powerful geospatial capabilities that are worth considering. The best tool is the one you have with you, and with these open-source libraries, you can have a pretty powerful toolbox wherever you go.