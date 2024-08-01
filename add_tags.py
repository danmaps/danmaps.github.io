import os
import yaml

# Directory containing your markdown files
output_dir = "posts"

# Define a mapping of keywords to tags
tag_mapping = {
    "Python": ["Python", "Programming"],
    "GIS": ["GIS", "Geospatial"],
    "Automation": ["Automation", "Workflow"],
    "Map": ["Mapping", "Cartography"],
    "Introduction": ["Introduction", "Overview"],
    "ArcGIS": ["ArcGIS", "Esri"],
    "Data Science": ["Data Science", "Machine Learning"],
    "SQL": ["SQL", "Database"],
    "ArcGIS Pro": ["ArcGIS Pro", "Esri"],
    "AI": ["AI", "Generative AI"],
    "Machine Learning": ["Machine Learning", "AI"],
    "Spatial Analysis": ["Spatial Analysis"],
    # Add more mappings as needed
}

# Function to determine tags based on the title
def determine_tags(title):
    tags = []
    for keyword, keyword_tags in tag_mapping.items():
        if keyword.lower() in title.lower():
            tags.extend(keyword_tags)
    return list(set(tags))  # Remove duplicates

# Update each markdown file with tags
for filename in os.listdir(output_dir):
    if filename.endswith('.md'):
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            front_matter, body = content.split('---\n', 2)[1:3]
            metadata = yaml.safe_load(front_matter)

        # Determine tags based on the title
        tags = determine_tags(metadata.get('title', ''))
        metadata['tags'] = tags

        # Write back the updated front matter and content
        new_front_matter = yaml.dump(metadata, default_flow_style=False).strip()
        new_content = f"---\n{new_front_matter}\n---\n{body}"
        with open(file_path, 'w') as file:
            file.write(new_content)
