import argparse
from pathlib import Path

import requests

from upload_insta import download_image


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id запуска')
    parser.add_argument('--download_path', help='Путь куда надо скачать изображения', default='images')

    return parser


def fetch_spacex():
    parser = create_parser()
    args = parser.parse_args()
    launch_id = args.id
    download_path = args.download_path

    Path(download_path).mkdir(parents=True, exist_ok=True)

    spacex_url = f'https://api.spacexdata.com/v3/launches/{launch_id}'
    response = requests.get(spacex_url)
    response.raise_for_status()

    links = response.json()['links']
    spacex_images_urls = links['flickr_images']

    for number, spacex_image_url in enumerate(spacex_images_urls, start=1):
        filename = f'spacex{number}.jpg'
        download_image(spacex_image_url, download_path, filename)


if __name__ == '__main__':
    fetch_spacex()
