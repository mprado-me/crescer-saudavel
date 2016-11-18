#!/bin/bash

sudo apt-get update;
sudo apt-get install -y python python-pip python-virtualenv;
sudo apt-get install -y postgresql postgresql-contrib
sudo apt-get install -y python-psycopg2
sudo apt-get install -y libpq-dev
sudo apt-get install -y python-dev

cd /vagrant;
sudo virtualenv env --always-copy;
source env/bin/activate;
pip install --upgrade pip;
pip install Flask;
pip install Flask-WTF;
pip install Flask-SQLAlchemy;
pip install flask-bcrypt;
pip install psycopg2;
pip install Flask-Mail;
pip install Flask-Login;

cd /vagrant;
mkdir logs;
mkdir uploads;

# To create database user and the database for the user:
# >> sudo su - postgres
# >> psql
# >> create user <username> with password '<password>';
# >> create database <database_name> owner <username>;