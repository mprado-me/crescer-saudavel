#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "login"

# The order of this import matter. models.py uses bcrypt and db
from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

import views.user_management
import views.products
import views.cart
import views.blog
import flask_app.views.user
import flask_app.views.admin

import models