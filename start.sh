. env/bin/activate
cp -R static /tmp/
cp configs/agstlogger.uwsgi.ini agstlogger.ini
uwsgi --ini agstlogger.ini && echo "started: agstlogger"
