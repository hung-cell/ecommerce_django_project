# Started with E-Commerce Application using django
## Enviroment
First you need to set up virtual enviroment to install django in your computer.<br />
1/ Create Virtual Environment
```bash
python -m venv env
````
2/ Activate Virtual Environment
```bash
source env/bin/activate  
```
You may not need to setup environment but I recommend you to do it so as not to conflict with other python projects on your machine.

## Install Django
You need install Django-4.0.4 to make sure the project can run
```bash
pip install Django==4.0.4
```
You also need to install Pillow-9.1.0 to use ImageFiled
```bash
pip install Pillow==9.1.0
```
## Migrate
You need to apply migrations to your project
```bash
python manage.py migrate
```
## Run project
```bash
python manage.py runserver
```
Publics project to address http://localhost:8000 .
It should be ready to go.

## Note
There is no initial data so you need to create your own data, go to  http://localhost:8000/admin, click product and create your own product. You may need
to create superuser to access admin. i recommend you google search :))

