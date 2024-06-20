"""
Convenience script(s) to
Card upgrade ids from the -previously downloaded, "constants" card upgrade .cs file
"""

import json
import os
import re


def parse_cs_file(filepath):
    upgrade_data = {}

    # Regular expression to capture asset name and GUID
    pattern = re.compile(r'public static readonly string (\w+) = "([0-9a-f\-]+)";')

    with open(filepath, "r") as file:
        lines = file.readlines()
        for line in lines:
            match = pattern.search(line)
            if match:
                asset_name = match.group(1)
                guid = match.group(2)
                upgrade_data[guid] = {
                    "from_file": "VanillaCardUpgradeDataIDs",
                    "asset_name": asset_name,
                    "asset_string": asset_name,
                }

    return upgrade_data


def main():
    # Define the paths
    current_directory = os.path.dirname(os.path.abspath(__file__))
    cs_file_path = os.path.join(
        current_directory, "constants", "VanillaCardUpgradeDataIDs.cs"
    )
    json_file_path = os.path.join(current_directory, "upgrade_ids.json")

    # Parse the .cs file
    upgrade_data = parse_cs_file(cs_file_path)

    # Write the parsed data to the JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(upgrade_data, json_file, indent=4)


if __name__ == "__main__":
    main()
