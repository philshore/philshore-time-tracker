export PGPASSWORD=agstloggerpassword
sudo locale-gen en_PH.UTF-8
sudo apt-get update
sudo apt-get autoremove -y install-info

sudo apt-get update

ppaexists=$( grep ^ /etc/apt/sources.list /etc/apt/sources.list.d/* | grep postgres )
echo "Configuring and install postgresql"
if [ ! $ppaexists ]; then
        echo "Add PostgreSQL PPA..."
        sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main"
        sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
        sudo apt-get update
else
        echo "PostgreSQL PPA already exists..."
fi

echo "Setting postgresql"
sudo apt-get install -y postgresql-9.6
sudo service postgresql start
sudo -u postgres psql -c "CREATE USER agstloggeruser WITH PASSWORD 'agstloggerpassword';"
sudo -u postgres psql -c "ALTER ROLE agstloggeruser WITH SUPERUSER;"
sudo -u postgres createdb -O agstloggeruser agstloggerdb -E utf-8

echo "Installing other system libraries"
sudo apt-get install -y libpq-dev python3-psycopg2 python3-dev python3-venv python-pip libssl-dev libffi-dev libxml2-dev libxslt-dev virtualenv redis-server libfontconfig nginx

echo "Setting up python libraries"
virtualenv -p python3 env
. env/bin/activate
pip install -r requirements.txt

agstlogger_backups=backups
echo $agstlogger_backups 
if [ -d "$agstlogger_backups" ]; then
  cd backups/
  psql -h localhost -U agstloggeruser -d agstloggerdb < dtrdb_backup_06_27_2017
else
  python manage.py migrate
fi

sudo mkdir -p /var/log/agstlogger
sudo chmod -R 777 /var/log/agstlogger



