# Космический Инстаграм

Пара скриптов для скачивания фотографий c помощью Api c сайтов [Hubble](https://hubblesite.org/api/v3/images/) 
и [SpaceX](https://api.spacexdata.com/v3/launches/).

И один скрипт для загрузки фотографий в Instagram.


## Запуск

Для запуска скриптов вам понадобится Python3.

Скачайте код с GitHub.

Установите зависимости:

`pip3 install -r requirements.txt`

Затем можно использовать два скрипта.

Скрипт `fetch_spacex.py` нужно запускать с `id` запуска, например:

`python3 fetch_spacex.py 25`

По умолчанчию изображения скачиваются в папку `images`.

Можно добавить опциональный аргумент `--download_path`, чтобы указать куда загружать изображения, например:

`python3 fetch_spacex.py 25 --download_path spacex_images`

Скрипт `fetch_hubble.py` нужно запускать с названием коллекции, например:

`python3 fetch_hubble.py spacecraft` 

По умолчанчию изображения скачиваются в папку `images`.

Можно добавить опциональный аргумент `--download_path`, чтобы указать куда загружать изображения, например:

`python3 fetch_hubble.py spacecraft --download_path hubble_images`

Скрипт `upload_insta.py` загрузит изображения в ваш профиль Instagram. По умолчанию скрипт пытается найти изображения
в папке `images`, но можно указать свой путь с помощью аргумента `--path`, например:

`python3 upload_insta.py --path /my_folder/my_images_for_insta`


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с остальными
скриптами и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Необходимые переменные:
- `INSTAGRAM_USERNAME` - имя пользователя в Instagram нужно для логина в аккаунт
- `INSTAGRAM_PASSWORD` - пароль пользователя в Instagram нужно для логина в аккаунт
- `IMAGES_PATH` - путь до изображений, которые надо загрузить в Instagram


## Используемые библиотеки

* [requests](https://pypi.org/project/requests/) - для запросов к API

* [python-dotenv](https://pypi.org/project/python-dotenv/) - для обращения к переменным окружения

* [Pillow](https://pypi.org/project/Pillow/) - для работы с изображениями

* [instabot](https://pypi.org/project/instabot/) - для загрузки изображений в Instagram


## Цели проекта

Devman. API веб-сервисов. Четвертый урок.

Сайт реализован в рамках курса по Django на [devman](https://dvmn.org/modules/).
