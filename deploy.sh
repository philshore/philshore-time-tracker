sudo cp configs/agstlogger.nginx /etc/nginx/sites-available/agstlogger
sudo ln -s /etc/nginx/sites-available/agstlogger /etc/nginx/sites-enabled/agstlogger
sudo rm /etc/nginx/sites-enabled/default
cp configs/agstlogger.uwsgi.ini agstlogger.ini
sudo service nginx restart