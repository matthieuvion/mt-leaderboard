"""
Convenience file to
Download constants ressources from Trainworks2 constants directory :
https://github.com/brandonandzeus/Trainworks2/tree/master/TrainworksModdingTools/ConstantsV2
"""

import os
import requests


def download_file(url, local_path):
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


def download_directory(api_url, local_dir):
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    response = requests.get(api_url)
    response.raise_for_status()
    directory_content = response.json()

    for item in directory_content:
        item_url = item["download_url"]
        item_path = os.path.join(local_dir, item["name"])
        if item["type"] == "file":
            print(f"Downloading {item_url} to {item_path}")
            download_file(item_url, item_path)
        elif item["type"] == "dir":
            new_local_dir = os.path.join(local_dir, item["name"])
            new_api_url = item["url"] + "?ref=857debf494fbe5bfcc5fd195a14b292c264f0d62"
            download_directory(new_api_url, new_local_dir)


if __name__ == "__main__":
    repo_url = "https://api.github.com/repos/brandonandzeus/Trainworks2/contents/TrainworksModdingTools/ConstantsV2"
    local_dir = "ConstantsV2"
    download_directory(
        repo_url + "?ref=857debf494fbe5bfcc5fd195a14b292c264f0d62", local_dir
    )
