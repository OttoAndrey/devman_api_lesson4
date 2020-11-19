import argparse
from pathlib import Path

import requests

from upload_insta import download_image


def fetch_spacex():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id запуска')
    args = parser.parse_args()
    launch_id = args.id
    path = 'images'

    Path(path).mkdir(parents=True, exist_ok=True)

    spacex_url = f'https://api.spacexdata.com/v3/launches/{launch_id}'
    response = requests.get(spacex_url)
    response.raise_for_status()

    links = response.json()['links']
    spacex_images_urls = links['flickr_images']

    for number, spacex_image_url in enumerate(spacex_images_urls, start=1):
        filename = f'spacex{number}.jpg'
        download_image(spacex_image_url, path, filename)


if __name__ == '__main__':
    fetch_spacex()
