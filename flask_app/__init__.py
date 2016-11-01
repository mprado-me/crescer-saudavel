#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

mail = Mail(app)

import flask_app.views.user

import models