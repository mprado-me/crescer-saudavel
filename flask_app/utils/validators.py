#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..models.user import User

from wtforms.validators import ValidationError
from exceptions import DatabaseAccessError

class CorrectPassword(object):
    def __init__(self, message=u'Senha incorreta'):
        self.message = message

    def __call__(self, form, field):
        try:
            user = User.query.filter(User.email == form.email.data).first()
        except:
            raise DatabaseAccessError()
        incorrect_password = False
        if user:
            incorrect_password = not user.is_correct_password(field.data)
        if incorrect_password:
            raise ValidationError(self.message)

class NotUnique(object):
    def __init__(self, model, field, message=u'Elemento é único'):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        try:
            check = self.model.query.filter(self.field == field.data).first()
        except:
            raise DatabaseAccessError()
        if not check:
            raise ValidationError(self.message)


class Unique(object):
    def __init__(self, model, field, message=u'Elemento já existente'):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        try:
            check = self.model.query.filter(self.field == field.data).first()
        except:
            raise DatabaseAccessError()
        if check:
            raise ValidationError(self.message)


class VariableTrue(object):
    def __init__(self, model, key_field, var_field, message=u'Variável não é verdadeira'):
        self.model = model
        self.key_field = key_field
        self.var_name = str(var_field).split('.')[-1]
        self.message = message

    def __call__(self, form, field):
        try:
            model_instance = self.model.query.filter(self.key_field == field.data).first()
        except:
            raise DatabaseAccessError()
        if model_instance and getattr(model_instance, self.var_name) != True:
            raise ValidationError(self.message)
