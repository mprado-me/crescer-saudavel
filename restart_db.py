#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import db

db.drop_all()
db.create_all()
