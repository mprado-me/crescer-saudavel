#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db


class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer)
    name = db.Column(db.String(64))
