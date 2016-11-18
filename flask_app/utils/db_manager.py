#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db

from ..utils.exceptions import DatabaseAccessError

from ..models.user import User

class DbManager:
    def __init__(self):
        pass

    def add_user(self, user):
        try:
            db.session.add(user)
        except:
            raise DatabaseAccessError()

    def get_user(self, email):
        try:
            return User.query.filter_by(email=email).first()
        except:
            raise DatabaseAccessError()

    def commit(self):
        try:
            db.session.commit()
        except:
            raise DatabaseAccessError()

    def rollback(self):
        db.session.rollback()

db_manager = DbManager()