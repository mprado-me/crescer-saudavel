#!/bin/bash

sudo apt-get update;
sudo apt-get install -y python python-pip python-virtualenv;
sudo pip install --upgrade pip;
cd /vagrant;
sudo virtualenv env --always-copy;
source /vagrant/env/bin/activate;
pip install Flask;
pip install Flask-WTF;