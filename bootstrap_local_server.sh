#!/bin/bash

sudo apt-get update;
sudo apt-get install -y python python-pip;
sudo apt-get install -y postgresql postgresql-contrib
sudo apt-get install -y python-psycopg2
sudo apt-get install -y libpq-dev
sudo apt-get install -y python-dev
sudo pip install --upgrade pip;
sudo pip install Flask;
sudo pip install Flask-WTF;
sudo pip install Flask-SQLAlchemy;
sudo pip install flask-bcrypt;
sudo pip install psycopg2;
sudo pip install Flask-Mail;

# To create database user and the database for the user:
# >> sudo su - postgres
# >> psql
# >> create user <username> with passowrd '<password>';
# >> create database <database_name> owner <username>;