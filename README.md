# English_Bot: Python telegram Bot for communicate with teacher

### This is simple telegram-bot for communicate on English lessons with teacher (Python + Django + Telegram API)
### Python telegram Bot v.1.0\
...

Файл зависимостей для pip pip-requirements.txt

Старт django project: django-admin startproject tga

###### Необходимые команды:
Overall HELP to check available subcommands:
python tga/manage.py -h  

Bot work as management command Django:
python tga/manage.py startapp ugc

Command to create/migrate migration:
python tga/manage.py -h makemigrations
python tga/manage.py -h migrate - it apply migration to database

###### Management commands(start local beck-end server):
Run server, local server:
python tga/manage.py runserver
http://127.0.0.1:8000/admin
Credentials:
Create default user for app (superuser User: admin Password: 123 )
python tga/manage.py createsuperuser

###### Telegram API access:
TOKEN = '5671088740:AAHC3GJT9Z778YDZAgp4vV_LDfK88DcmSlA'
PROXY_URL = 'https://core.telegram.org/bots/api'
