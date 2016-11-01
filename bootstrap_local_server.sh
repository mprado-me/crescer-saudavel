#!/bin/bash

sudo apt-get update;
sudo apt-get install -y python python-pip;
sudo pip install --upgrade pip;
pip install Flask;
pip install Flask-WTF;