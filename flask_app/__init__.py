#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask import Flask

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

import flask_app.views.user