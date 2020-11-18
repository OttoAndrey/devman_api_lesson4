# Космический Инстаграм

Пара скриптов для скачивания фотографий c помощью Api c сайтов [Hubble](https://hubblesite.org/api/v3/images/) 
и [SpaceX](https://api.spacexdata.com/v3/launches/).

И один скрипт для загрузки фотографий в Instagram.


## Запуск

Для запуска скрипта вам понадобится Python3.

Скачайте код с GitHub.

Установите зависимости:

`pip3 install -r requirements.txt`

Затем можно использовать два скрипта.

Скрипт `fetch_spacex.py` нужно запускать с `id` запуска, например:

`python3 fetch_spacex.py 25`

Скрипт `fetch_hubble.py` нужно запускать с названием коллекции, например:

`python3 fetch_hubble.py spacecraft` 

Изображения скачаются в папку `images`. Затем можно загрузить фотографии в свой профиль Instagram.

`python3 upload_insta.py`

Изображения будут отформатированы специально для Instagram и помещены в отдельную папку `insta_images`.


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с остальными
скриптами и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Необходимые переменные:
- `INSTAGRAM_USERNAME` - имя пользователя в Instagram нужно для логина в аккаунт
- `INSTAGRAM_PASSWORD` - пароль пользователя в Instagram нужно для логина в аккаунт

## Используемые библиотеки

* [requests](https://pypi.org/project/requests/) - для запросов к [Api](https://dev.bitly.com/api-reference) Bitly

* [python-dotenv](https://pypi.org/project/python-dotenv/) - для обращения к переменным окружения

* [Pillow](https://pypi.org/project/Pillow/) - для работы с изображениями

* [instabot](https://pypi.org/project/instabot/) - для загрузки изображений в Instagram


## Цели проекта

Devman. API веб-сервисов. Четвертый урок.

Сайт реализован в рамках курса по Django на [devman](https://dvmn.org/modules/).
