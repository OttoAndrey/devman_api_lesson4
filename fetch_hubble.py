import argparse
import os
from pathlib import Path

import requests

from upload_insta import download_image


def fetch_hubble_image(image_id, path):
    hubble_url = f'https://hubblesite.org/api/v3/image/{image_id}'

    response = requests.get(hubble_url)
    response.raise_for_status()

    image_files = response.json()['image_files']
    last_image_file = image_files[-1]
    last_image_url = f'https:{last_image_file["file_url"]}'
    root_ext_image_url = os.path.splitext(last_image_url)
    filename = f'{image_id}{root_ext_image_url[1]}'
    download_image(last_image_url, path, filename)


def fetch_hubble():
    parser = argparse.ArgumentParser()
    parser.add_argument('collection_name', help='Название коллекции фотографий')
    args = parser.parse_args()
    collection_name = args.collection_name

    path = 'images'
    Path(path).mkdir(parents=True, exist_ok=True)

    collection_url = f'https://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(collection_url)
    response.raise_for_status()

    for image in response.json():
        fetch_hubble_image(image['id'], path)


if __name__ == '__main__':
    fetch_hubble()
