#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    category_id = db.Column(db.Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="subcategories")
