Python telegram Bot v.1.0

nano pip-requirements.txt

Start django project: django-admin startproject tga

python tga/manage.py -h

python tga/manage.py startapp ugc

Create migration:
python tga/manage.py -h makemigrations

Migrate - it create migration in database:
python tga/manage.py -h migrate

Management command turn on app, run server:
python tga/manage.py runserver
http://127.0.0.1:8000/admin

Create default user(superuser U:admin P:123):
python tga/manage.py createsuperuser

