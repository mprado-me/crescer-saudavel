#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import db

from sqlalchemy import ForeignKey


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("category.id"))
    subcategory_id = db.Column(db.Integer, ForeignKey("subcategory.id"))
    price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.UnicodeText, nullable=False)

    image_1 = db.Column(db.Text, nullable=False)
    image_2 = db.Column(db.Text)
    image_3 = db.Column(db.Text)
    image_4 = db.Column(db.Text)
    image_5 = db.Column(db.Text)
    image_6 = db.Column(db.Text)
    image_7 = db.Column(db.Text)
    image_8 = db.Column(db.Text)
    image_9 = db.Column(db.Text)
    image_10 = db.Column(db.Text)

    tab_1_title = db.Column(db.String(32))
    tab_1_content = db.Column(db.UnicodeText)
    tab_2_title = db.Column(db.String(32))
    tab_2_content = db.Column(db.UnicodeText)
    tab_3_title = db.Column(db.String(32))
    tab_3_content = db.Column(db.UnicodeText)
    tab_4_title = db.Column(db.String(32))
    tab_4_content = db.Column(db.UnicodeText)
    tab_5_title = db.Column(db.String(32))
    tab_5_content = db.Column(db.UnicodeText)
    tab_6_title = db.Column(db.String(32))
    tab_6_content = db.Column(db.UnicodeText)
    tab_7_title = db.Column(db.String(32))
    tab_7_content = db.Column(db.UnicodeText)
    tab_8_title = db.Column(db.String(32))
    tab_8_content = db.Column(db.UnicodeText)
    tab_9_title = db.Column(db.String(32))
    tab_9_content = db.Column(db.UnicodeText)
    tab_10_title = db.Column(db.String(32))
    tab_10_content = db.Column(db.UnicodeText)
