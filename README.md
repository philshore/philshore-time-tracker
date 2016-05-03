# PhilSHORE Time Tracker App
A time logger application used by the PhilSHORE team.

## Setup
- Create a virtualenv using: ```virtualenv env```
- Activate the virtualenv using: ```source env/bin/activate```
- Install python packages: ```pip install -r requirements.txt```
- Create the database: ```python manage.py migrate```
- Create an admin: ```python manage.py createsuperuser```
- Run the dev server: ```python manage.py runserver```
