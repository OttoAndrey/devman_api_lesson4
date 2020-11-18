import argparse
from pathlib import Path

import requests

from upload_insta import fetch_hubble_image


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
