#!/bin/bash

cd /vagrant;
git pull;
sudo /etc/init.d/nginx restart;
cd /vagrant;
gunicorn flask_app:app -b localhost:8000

# Não usar virtual env no server de produção