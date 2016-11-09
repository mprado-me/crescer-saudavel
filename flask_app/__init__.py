#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For don't need digit .decode('utf-8') in all strings in template files
# http://stackoverflow.com/questions/24566538/flask-rendering-unicode-characters-in-template
import sys

if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')

import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

mail = Mail(app)

# Configuring log_route
handler = TimedRotatingFileHandler(
    filename=app.config['LOGGING_FILENAME'],
    when='D',
    interval=10,
    backupCount=5
)
handler.setLevel(app.config['LOGGING_LEVEL'])
formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# The order of this import matter. User uses bcrypt and db
from models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


import models.user

import views.admin
import views.blog
import views.cart
import views.general
import views.products
import views.user_management
