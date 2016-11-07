#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
login_manager.login_view =  "login"

mail = Mail(app)

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

