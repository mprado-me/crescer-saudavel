#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), unique=True)
