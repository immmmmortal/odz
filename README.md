# odz
# Installation

1. - clone the project
 ```
  git clone https://github.com/immmmmortal/odz.git
 ```
2. - create and start a a virtual environment
 ```
   virtualenv env --no-site-packages
   source env/bin/activate
 ```
3. - Install the project dependencies:
```
   pip install -r requirements.txt
```
4. - Create .env
```
   touch .env
```
5. - obtain a secret from [(https://miniwebtool.com/django-secret-key-generator/)](https://djecrety.ir/) key and add to secrets.sh
6. - add secret to .env
7. - add .env to .gitignore file
8. - then run
```
   python manage.py migrate
```
9 - To create admin account
```
    python manage.py createsuperuser
```
10.- Then to makemigrations for the app
```
    python manage.py makemigrations ig_miner_app
```
11. - Again run migrate
```
   python manage.py migrate
 ```
12. - Project readt for development, to start the development server run:
```
    python manage.py runserver
```
