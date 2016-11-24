#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db

from ..utils.exceptions import DatabaseAccessError

from ..models.category import Category
from ..models.product import Product
from ..models.subcategory import Subcategory
from ..models.user import User

class DbManager:
    def __init__(self):
        pass

    def add(self, element):
        try:
            db.session.add(element)
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def delete(self, element):
        try:
            db.session.delete(element)
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def get_user(self, email):
        try:
            return User.query.filter_by(email=email).one_or_none()
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def get_category(self, category_id):
        try:
            return Category.query.filter_by(id=category_id).one_or_none()
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def get_subcategory(self, subcategory_id):
        try:
            return Subcategory.query.filter_by(id=subcategory_id).one_or_none()
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def get_product(self, product_id):
        try:
            return Product.query.filter_by(id=product_id).one_or_none()
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def refresh(self, element):
        try:
            db.session.refresh(element)
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def commit(self):
        try:
            db.session.commit()
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def rollback(self):
        db.session.rollback()

db_manager = DbManager()
