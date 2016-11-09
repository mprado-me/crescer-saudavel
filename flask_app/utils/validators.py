#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms.validators import ValidationError
from exceptions import DatabaseAccessError

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