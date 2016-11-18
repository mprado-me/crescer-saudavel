#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from ..models.user import User

from exceptions import DatabaseAccessError

from flask import request

from wtforms.validators import HostnameValidation, ValidationError, Regexp, StopValidation


class AllowedFileFormat(object):
    def __init__(self, input_file_name, allowed_extensions, message=u'Formato de arquivo inválido', stop=False):
        self.input_file_name = input_file_name
        self.allowed_extensions = allowed_extensions
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        current_file = request.files[self.input_file_name]
        filename = current_file.filename
        allowed_file = '.' in filename and filename.rsplit('.', 1)[1] in self.allowed_extensions

        if not allowed_file:
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)


class CorrectPassword(object):
    def __init__(self, message=u'Senha incorreta', stop=False):
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        try:
            user = User.query.filter(User.email == form.email.data).first()
        except:
            raise DatabaseAccessError()
        incorrect_password = False
        if user:
            incorrect_password = not user.is_correct_password(field.data)
        if incorrect_password:
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)


class Email(Regexp):
    def __init__(self, message="Formato de email inválido", stop=False):
        self.message = message
        self.stop = stop
        self.validate_hostname = HostnameValidation(
            require_tld=True,
        )
        super(Email, self).__init__(r'^.+@([^.@][^@]+)$', re.IGNORECASE, message)

    def __call__(self, form, field):
        try:
            match = super(Email, self).__call__(form, field, self.message)
        except ValidationError:
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)

        if not self.validate_hostname(match.group(1)):
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)


class HasFilePart(object):
    def __init__(self, input_file_name, message=u'Nenhum arquivo foi selecionado', stop=False):
        self.input_file_name = input_file_name
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        has_file_part = self.input_file_name in request.files
        current_file = request.files[self.input_file_name]
        valid_filename = current_file.filename != ''

        if (not has_file_part) or (not valid_filename):
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)


class Length(object):
    def __init__(self, min_length=-1, max_length=-1, message=None, stop=False):
        assert min_length != -1 or max_length != -1, 'At least one of `min` or `max` must be specified.'
        assert max_length == -1 or min_length <= max_length, '`min` cannot be more than `max`.'
        self.min = min_length
        self.max = max_length
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            message = self.message
            if message is None:
                if self.max == -1:
                    message = field.ngettext('O campo deve possuir no mínimo %(min)d caracter',
                                             'O campo deve possuir no mínimo %(min)d caracteres', self.min)
                elif self.min == -1:
                    message = field.ngettext('O campo deve possuir no máximo %(max)d caracter',
                                             'O campo deve possuir no máximo %(max)d caracteres', self.max)
                else:
                    message = field.gettext('O campo deve possuir entre %(min)d e %(max)d caracteres')

            if self.stop:
                raise StopValidation(message % dict(min=self.min, max=self.max, length=l))
            else:
                raise ValidationError(message % dict(min=self.min, max=self.max, length=l))


class NotUnique(object):
    def __init__(self, model, field, message=u'Elemento é único', stop=False):
        self.model = model
        self.field = field
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        try:
            check = self.model.query.filter(self.field == field.data).first()
        except:
            raise DatabaseAccessError()
        if not check:
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)


class Unique(object):
    def __init__(self, model, field, message=u'Elemento já existente', stop=False):
        self.model = model
        self.field = field
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        try:
            check = self.model.query.filter(self.field == field.data).first()
        except:
            raise DatabaseAccessError()
        if check:
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)


class VariableFalse(object):
    def __init__(self, model, key_field, var_field, message=u'Variável não é falsa', stop=False):
        self.model = model
        self.key_field = key_field
        self.var_name = str(var_field).split('.')[-1]
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        try:
            model_instance = self.model.query.filter(self.key_field == field.data).first()
        except:
            raise DatabaseAccessError()
        if model_instance and getattr(model_instance, self.var_name) is not False:
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)


class VariableTrue(object):
    def __init__(self, model, key_field, var_field, message=u'Variável não é verdadeira', stop=False):
        self.model = model
        self.key_field = key_field
        self.var_name = str(var_field).split('.')[-1]
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        try:
            model_instance = self.model.query.filter(self.key_field == field.data).first()
        except:
            raise DatabaseAccessError()
        if model_instance and getattr(model_instance, self.var_name) is not True:
            if self.stop:
                raise StopValidation(self.message)
            else:
                raise ValidationError(self.message)
