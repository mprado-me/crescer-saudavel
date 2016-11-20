#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db

from ..utils.exceptions import DatabaseAccessError

from ..models.category import Category
from ..models.user import User

class DbManager:
    def __init__(self):
        pass

    def add_user(self, user):
        try:
            db.session.add(user)
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def get_user(self, email):
        try:
            return User.query.filter_by(email=email).first()
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def add_category(self, category):
        try:
            db.session.add(category)
        except Exception as e:
            raise DatabaseAccessError(exception=e)

    def get_category(self, category_id):
        try:
            return Category.query.filter_by(id=category_id).first()
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
