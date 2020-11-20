import argparse
import os
import shutil
from pathlib import Path

import instabot
import requests
from PIL import Image
from dotenv import load_dotenv


def download_image(url, path, filename):
    Path(path).mkdir(parents=True, exist_ok=True)

    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(f'{path}/{filename}', 'wb') as file:
        file.write(response.content)


def create_parser():
    load_dotenv()

    images_path = os.getenv('IMAGES_PATH') or 'images'

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Путь до изображений', default=images_path)

    return parser


def upload_insta():
    load_dotenv()

    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')

    parser = create_parser()
    args = parser.parse_args()
    images_path = args.path

    insta_path = 'insta_images'
    Path(insta_path).mkdir(parents=True, exist_ok=True)

    images_names = os.listdir(images_path)

    for image_name in images_names:
        image = Image.open(f'{images_path}/{image_name}')
        image.thumbnail((1080, 1080))
        rgb_image = image.convert('RGB')
        root_ext_image_name = os.path.splitext(image_name)
        rgb_image.save(f'{insta_path}/{root_ext_image_name[0]}.jpg', format='JPEG')

    bot = instabot.Bot()
    bot.login(username=username, password=password)

    insta_images_names = os.listdir(insta_path)

    try:
        for insta_image_name in insta_images_names:
            bot.upload_photo(f'{insta_path}/{insta_image_name}')
    except Exception as e:
        print(e)
        print('Не все ваши фотографии удалось загрузить. Попробуйте еще раз позже.')
    finally:
        shutil.rmtree(insta_path)


if __name__ == '__main__':
    upload_insta()
