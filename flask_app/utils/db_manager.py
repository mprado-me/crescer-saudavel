#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db

from ..utils.exceptions import DatabaseAccessError

from ..models.user import User

class DbManager:
    def __init__(self):
        pass

    def add_user(self, email, password):
        try:
            user = User(
                email=email,
                password=password
            )
            db.session.add(user)
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
