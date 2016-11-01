#!/bin/bash

cd /vagrant
sudo mkdir instance
cd /vagrant/instance
sudo touch config.py
echo "DEBUG=False" >> config.py

sudo apt-get install -y python nginx gunicorn;
sudo /etc/init.d/nginx start;
sudo rm /etc/nginx/sites-enabled/default;
sudo rm /etc/nginx/sites-available/flask_app;
sudo rm /etc/nginx/sites-enabled/flask_app;
sudo cp /vagrant/ngix_config /etc/nginx/sites-available/flask_app;
sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled/flask_app;
sudo /etc/init.d/nginx restart;
cd /vagrant/flask_app/;

# to init production server:
# >> gunicorn flask_app:app -b localhost:8000