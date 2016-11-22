#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import db

from flask_app.models.subcategory import Subcategory

from sqlalchemy.orm import relationship


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    subcategories = relationship("Subcategory", order_by=Subcategory.name, back_populates="category", cascade="delete")
