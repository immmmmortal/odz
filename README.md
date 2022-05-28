# odz


Installation

1. clone the project
 
  https://github.com/immmmmortal/odz.git
 
2. create and start a a virtual environment

  virtualenv env --no-site-packages
  
  source env/bin/activate
  
3. Install the project dependencies:

  pip install -r requirements.txt

4. Create secrets.sh

  touch secrets.sh
  
5. obtain a secret from [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/) key and add to secrets.sh

6. add secret to secrets.sh
7. add secrets.sh to .gitignore file
8. then run

python manage.py migrate

create admin account

python manage.py createsuperuser

9.then to makemigrations for the app

python manage.py makemigrations ig_miner_app

10.again run migrate

python manage.py migrate
 
11. Project readt for development, to start the development server run:

python manage.py runserver
