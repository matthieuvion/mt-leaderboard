"""
Convenience script(s) to
Retrieve covenant ids from the -previously downloaded, "constants" covenent .cs file
"""

import json
import os
import re

# Get the current running directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the file paths
cs_file_path = os.path.join(current_directory, "constants", "VanillaCovenentIDs.cs")
json_file_path = os.path.join(current_directory, "covenant_ids.json")

# Print the current working directory for debugging
print(f"Current working directory: {current_directory}")
print(f"Expected .cs file path: {cs_file_path}")

# Check if the .cs file exists
if not os.path.exists(cs_file_path):
    print(f"File not found: {cs_file_path}")
    exit(1)

# Read the .cs file
with open(cs_file_path, "r") as file:
    lines = file.readlines()

# Initialize a dictionary to store the parsed data
covenant_ids = {}

# Define regex patterns to extract the needed information
pattern_id = re.compile(r'public static readonly string (\w+) = "(.*?)";')
pattern_asset_name = re.compile(r"/// Asset name: (\w+)")

# Parse the lines
for i, line in enumerate(lines):
    match_id = pattern_id.search(line)
    if match_id:
        asset_string = match_id.group(1)
        id_value = match_id.group(2)
        asset_name = ""
        # Search for the asset name in the preceding lines
        for j in range(i - 1, -1, -1):
            match_asset_name = pattern_asset_name.search(lines[j])
            if match_asset_name:
                asset_name = match_asset_name.group(1)
                break

        covenant_ids[id_value] = {
            "from_file": "VanillaCovenentIDs",
            "asset_name": asset_name,
            "asset_string": asset_string,
        }

# Write the dictionary to a JSON file
with open(json_file_path, "w") as json_file:
    json.dump(covenant_ids, json_file, indent=4)

print(f"JSON file saved to {json_file_path}")
