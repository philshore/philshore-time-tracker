# PhilSHORE Time Tracker App
A time logger application used by the PhilSHORE team.

## Development Requirements
- Vagrant
- Virtualbox

## Deployment Requirements
- Python 3
- Nginx
- Ubuntu 16.04
- Postgres

## Development Setup
1. Clone this repository:
```
git clone https://github.com/philshore/philshore-time-tracker.git
```
2. In your terminal/command prompt, go into the cloned directory:
```
cd philshore-time-tracker
```
3. Run vagrant:
```
vagrant up
```
4. Login to vagrant
```
vagrant ssh
```
5. Go into the src directory:
```
cd src
```
6. Activate virtualenv
```
. env/bin/activate
```
7. Run the developmental server
```
python manage.py runserver 0.0.0.0:8000
```
8. In your browser, access http://127.0.0.1:8000

## Deployment(Ubuntu 16.04 LTS)
1. Clone this repository:
```
git clone https://github.com/philshore/philshore-time-tracker.git
```
2. Go into the cloned directory
```
cd philshore-time-tracker
```
3. Install the necessary libraries
```
sh install.sh
```
4. Run the deployment script:
```
sh deploy.sh
```
5. Run the start script:
```
sh start.sh
```
6. In your browser, access http://<ip-address>/
