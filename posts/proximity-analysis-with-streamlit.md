---
author: Danny McVey
categories:
- GIS
- Python Tutorials
date: 2024-07-01
layout: post
summary: Learn how to automate proximity analysis in GIS using Python.
tags:
- Spatial Analysis
- Python
- Streamlit
- Proximity Analysis
thumbnail: static/images/thumbnails/proximity-analysis.png
title: Automating Proximity Analysis in Streamlit with Open Source Python
---

I recently took on a work project that began with a simple goal: perform spatial proximity analysis for a user. Initially, this was a manual task using ArcGIS Pro, but I ended up turning it into a fully automated tool. Here's a detailed look at what I learned, how I refined user requirements, leveraged open-source tools, and ultimately turned this into a useful and flexible tool.

## The Manual Approach

Initially, I performed the analysis manually using ArcGIS Pro. This involved several time-consuming steps:

1. **Data Preparation**: Cleaning and organizing the data to ensure accuracy.
2. **Running Geoprocessing Tools**: Using ArcGIS Pro to perform spatial proximity analysis. This involves several ArcGIS geoprocessing tools, including the following:
    - **Near Table**: Identifying points within a specified distance of another point.
    - **Buffer**: Creating a buffer around each point.
    - **Dissolve**: Merging the buffers together to create distinct polygons representing each group.
    - **Spatial Join**: Joining the buffers with the original data to get the original attributes for each group and summing a field of interest.
3. **Creating a Web App**: Developing a web application in ArcGIS Online to display the results interactively.

[![](https://mermaid.ink/img/pako:eNpFUNtugkAQ_ZXNPGmCZEUQoUkTL01j0iam9qnAwxRW3ZRlybA0UvXfXalp52nOmTNnLifIdSEghj1hfWAvbw9pxWzMB8nTMRdlNmSj0eN5rWpNhmFVsFxX34LMmS2S5B0_S5Fl957FTbocJHPKn9dbtiGdDe-lZe-yEbTTpFhTo5FYspr0USppOmuMZdfI5sxWyX1wBg4oQQplYdc73XxSMAehRAqxTQukrxTS6mJ12Bq97aocYkOtcIB0uz9AvMOysaitCzRiJdHeqP5YUUij6fX3-v4JDtRYfWj9r7EY4hMcIQ4m3PWC2TgIp17Aw7EDnSV9N7JgEnHP55HHJxcHfvp-7s6sMvL9ceiF0TTks8sVcl9wLA?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpFUNtugkAQ_ZXNPGmCZEUQoUkTL01j0iam9qnAwxRW3ZRlybA0UvXfXalp52nOmTNnLifIdSEghj1hfWAvbw9pxWzMB8nTMRdlNmSj0eN5rWpNhmFVsFxX34LMmS2S5B0_S5Fl957FTbocJHPKn9dbtiGdDe-lZe-yEbTTpFhTo5FYspr0USppOmuMZdfI5sxWyX1wBg4oQQplYdc73XxSMAehRAqxTQukrxTS6mJ12Bq97aocYkOtcIB0uz9AvMOysaitCzRiJdHeqP5YUUij6fX3-v4JDtRYfWj9r7EY4hMcIQ4m3PWC2TgIp17Aw7EDnSV9N7JgEnHP55HHJxcHfvp-7s6sMvL9ceiF0TTks8sVcl9wLA)
            
While this approach worked, it was labor-intensive and required significant effort for each new dataset. It became clear that automating this process would save time and ensure consistency.

[![](https://mermaid.ink/img/pako:eNpFUMtuwjAQ_BVrTyAFZEJCHpUqFeitlaqiXkhyWMWbYDWOI8epSIF_r6Go3dPO7szs4wSlFgQp1Aa7A3t5f8hb5uJpkj0fS2qKKZvNHs8fXaNRMGwFK3X7Rcae2TrLatICLVYGFRXFXbq-KjaTbGcNoWqkLab3zubm9Uam0kaxvkMrsWGd0UeppB2dPTZjL_sz22b38QV4oMgolMItebr65GAPpCiH1KUCzWcOeXtxPBys3o1tCak1A3lg9FAfIK2w6R0aOrcqbSW6S9VflYS02rz-_uD2Cg86bPda_3MchvQER0jDJZ_7YbwIo5Uf8mjhweiKwTxxYJlwP-CJz5cXD75vej6PHTMJgkXkR8kq4vHlB7xoc3k?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpFUMtuwjAQ_BVrTyAFZEJCHpUqFeitlaqiXkhyWMWbYDWOI8epSIF_r6Go3dPO7szs4wSlFgQp1Aa7A3t5f8hb5uJpkj0fS2qKKZvNHs8fXaNRMGwFK3X7Rcae2TrLatICLVYGFRXFXbq-KjaTbGcNoWqkLab3zubm9Uam0kaxvkMrsWGd0UeppB2dPTZjL_sz22b38QV4oMgolMItebr65GAPpCiH1KUCzWcOeXtxPBys3o1tCak1A3lg9FAfIK2w6R0aOrcqbSW6S9VflYS02rz-_uD2Cg86bPda_3MchvQER0jDJZ_7YbwIo5Uf8mjhweiKwTxxYJlwP-CJz5cXD75vej6PHTMJgkXkR8kq4vHlB7xoc3k)    
            
## Refining User Requirements

I first needed to understand the users' needs better. I decided that users would need:

- The ability to upload their own datasets.
- Dynamic selection of columns for latitude, longitude, and IDs.
- Interactive adjustment of proximity thresholds.
- Immediate visualization and downloadable results.

These choices guided the development of a more robust tool.

## Leveraging Open-Source Tools as an Alternative to Arcpy

In my professional experience, I've extensively used Arcpy for geospatial analysis. However, I had to explore open-source alternatives for this project. I chose Geopandas for the analysis and Folium inside Streamlit for the UI, which offered several benefits:

- **Geopandas**: Provides powerful data structures for working with geospatial data in Python, similar to how Pandas handles tabular data. It enabled seamless conversion between dataframes and geospatial dataframes. Figuring ou how to match the geoprocessing operations avilable in ArcGIS Pro was a breakthrough.
- **Folium**: Facilitates the creation of interactive maps directly from geospatial data. It integrates well with Streamlit, allowing for a smooth user experience. I also knew that Streamlit allows for easy upload and download of data files including Excel.

The choice of these tools was influenced by their flexibility and the growing ecosystem of geospatial libraries in the open-source community. They provide a cost-effective and versatile alternative to proprietary solutions, aligning with the broader movement towards open-source in geospatial analysis. Crucially, this allows the tool to be run anywhere (including here on `streamlit.app`) because it does not depend on proprietary software licensing.

## Self-Serve Tool vs. Delivering Analysis Results

One of the key decisions I face (often) is whether to provide a self-serve tool or to deliver analysis results directly to customers. Each approach has its merits:

- **Self-Serve Tool**: Empowers users to explore their data independently. It's flexible and scalable, allowing users to upload their datasets, configure analysis parameters, and obtain results instantly. This approach aligns well with the trend towards democratizing data analysis.
- **Delivering Analysis Results**: Suitable for users who need specific insights without the need to interact with the tool. It involves processing the data on behalf of the user and delivering a polished report.

For this project, I created a self-serve tool, leveraging Streamlit's capabilities to create an interactive and user-friendly interface. This decision was based on the goal of enabling users to perform their analysis independently, saving everyone time and effort. Whether they'll actually want to use it in the future remains to be seen... Either way, I'm glad I have this tool to use for myself, and to potentially repurpose it in the future.

## The Automated Tool: A practical utility with a lot going on under the hood

Here's a brief overview of some of the functionality implemented in the automated tool:

### File Upload and Data Handling:
```python
def handle_file_upload():
    uploaded_file = st.file_uploader("Choose a .xlsx file", type="xlsx")
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.DataFrame(sample_data)  # Use sample data if no file is uploaded
    return df, uploaded_file
```

### Proximity Analysis:

```python
def process_data(df, lat_col, lon_col, distance_threshold, id_col=None):
    # Convert DataFrame to GeoDataFrame and set the coordinate reference system (CRS)
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[lon_col], df[lat_col]))
    projected_gdf = gdf.to_crs(epsg=32611)

    # Spatial analysis logic:
    # 1. Initialize spatial index for efficient querying of nearby points
    tree = projected_gdf.sindex

    # 2. Create a list to store the results
    nearby_points = []

    # 3. Iterate through each point in the GeoDataFrame
    for index, row in projected_gdf.iterrows():
        # 4. Create a buffer around each point with the given distance threshold
        buffer = row.geometry.buffer(distance_threshold)

        # 5. Find all points within the buffer using the spatial index
        possible_matches_index = list(tree.intersection(buffer.bounds))
        possible_matches = projected_gdf.iloc[possible_matches_index]

        # 6. Filter these points to only include those within the exact distance threshold
        precise_matches = possible_matches[
            possible_matches.distance(row.geometry) <= distance_threshold
        ]

        # 7. Exclude the point itself from the results
        precise_matches = precise_matches[precise_matches.index != index]

        # 8. Collect information about each nearby point
        for _, pm_row in precise_matches.iterrows():
            nearby_point_info = {
                "index": index,
                "distance_feet": round(pm_row.geometry.distance(row.geometry) * 3.28084, 2),  # Convert distance to feet
            }
            if id_col:
                nearby_point_info[f"nearby_{id_col}"] = pm_row[id_col]
            nearby_points.append(nearby_point_info)

    # 9. Convert the list of results into a DataFrame
    nearby_df = pd.DataFrame(nearby_points)

    # 10. Merge the original GeoDataFrame with the nearby points DataFrame
    if not nearby_df.empty:
        processed_gdf = gdf.merge(nearby_df, how="left", left_index=True, right_on="index")
    else:
        processed_gdf = gdf

    return processed_gdf

```
### Details of Steps of Proximity Analysis

1. **Convert DataFrame to GeoDataFrame**: This converts the input DataFrame `df` into a GeoDataFrame `gdf` with geometry based on the latitude (`lat_col`) and longitude (`lon_col`) columns. The CRS is initially set to EPSG:4326 (WGS 84) and then projected to EPSG:32611 (UTM zone 11N) for accurate distance calculations.

2. **Spatial Indexing**: A spatial index (`tree`) is created for the projected GeoDataFrame to allow efficient spatial querying. 

<details>
  <summary>Why Use a Spatial Index?</summary>
  A spatial index is used for performance optimization. Without it, finding all nearby points for each point would require comparing each point against every other point, resulting in a quadratic number of distance calculations (O(n^2)). The spatial index reduces this complexity by quickly narrowing down the list of potential nearby points using spatial relationships (like bounding boxes).
</details>

3. **Buffer Creation and Matching**: For each point in the GeoDataFrame, a buffer with the specified distance threshold is created. The spatial index is used to find all possible points within the buffer bounds.

4. **Distance Filtering**: The possible matches are filtered to include only those within the exact distance threshold. The point itself is excluded from the matches.

5. **Result Collection**: Information about each nearby point, including the distance in feet and optional ID columns, is collected and stored in a list.

6. **Merge Results**: The results are converted to a DataFrame (`nearby_df`) and merged with the original GeoDataFrame (`gdf`) to create the final processed GeoDataFrame (`processed_gdf`).
            

### Interactive Map Creation:
```python
def create_folium_map(gdf, distance_threshold_meters, lat_col, lon_col, id_col):
    m = folium.Map(tiles="cartodb-dark-matter", width='100%', height='100%')
    folium_static(m)
```

### User Interface with Streamlit:
```python
st.set_page_config(page_title="Spatial Proximity Excel Enrichment", layout="wide")
distance_threshold_feet = st.slider("Distance threshold in feet", 25, 800, 100)
distance_threshold_meters = feet_to_meters(distance_threshold_feet)
```

## Conclusion

This project was a significant learning experience. By refining user requirements, exploring open-source alternatives, and thoughtfully choosing the right delivery model, I developed a robust and flexible tool for spatial proximity analysis. This automation not only saves time but also ensures consistency and reproducibility, making this kind of analysis trivial in the future.

So, while the initial manual process was effective, the automated tool has proven to be a far more efficient and user-friendly solution. It's a perfect example of how engineering a solution thoughtfully can lead to a genuinely useful product.
        