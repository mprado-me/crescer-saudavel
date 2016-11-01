#!/bin/bash

cd /vagrant;
git pull;
sudo /etc/init.d/nginx restart;
cd /vagrant/flask_app/;
gunicorn app:app -b localhost:8000