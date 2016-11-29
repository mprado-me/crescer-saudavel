#!/bin/bash

sudo apt-get update;
sudo apt-get install -y python python-pip;
sudo apt-get install -y postgresql postgresql-contrib;
sudo apt-get install -y python-psycopg2;
sudo apt-get install -y libpq-dev;
sudo apt-get install -y python-dev;

pip install --upgrade pip;
pip install Flask;
pip install Flask-WTF;
pip install Flask-SQLAlchemy;
pip install flask-bcrypt;
pip install psycopg2;
pip install Flask-Mail;
pip install Flask-Login;
pip install enum34;
pip install markdown;

mkdir /vagrant/logs;
mkdir /vagrant/flask_app/static/uploads;
mkdir /vagrant/flask_app/static/uploads/images;

# To create database user and the database for the user:
# >> sudo su - postgres
# >> psql
# >> create user <username> with password '<password>';
# >> create database <database_name> owner <username>;
# or
# >> sudo runuser -l postgres -c "psql -c \"create user <username> with password 'password'\"";
# >> sudo runuser -l postgres -c "psql -c \"create database <database_name> owner <username>\"";
