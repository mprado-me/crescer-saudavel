#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..models.user import User

from exceptions import DatabaseAccessError

from flask import request

from wtforms.validators import ValidationError


class AllowedFileFormat(object):
    def __init__(self, input_file_name, allowed_extensions, message=u'Formato de arquivo inválido'):
        self.input_file_name = input_file_name
        self.allowed_extensions = allowed_extensions
        self.message = message

    def __call__(self, form, field):
        has_file_part = self.input_file_name in request.files
        if has_file_part:
            current_file = request.files[self.input_file_name]
            filename = current_file.filename
            if filename != '':
                allowed_file = '.' in filename and \
                   filename.rsplit('.', 1)[1] in self.allowed_extensions

                if not allowed_file:
                    raise ValidationError(self.message)


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


class HasFilePart(object):
    def __init__(self, input_file_name, message=u'Nenhum arquivo foi selecionado'):
        self.input_file_name = input_file_name
        self.message = message

    def __call__(self, form, field):
        has_file_part = self.input_file_name in request.files
        current_file = request.files[self.input_file_name]
        valid_filename = current_file.filename != ''

        if (not has_file_part) or (not valid_filename):
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


class VariableFalse(object):
    def __init__(self, model, key_field, var_field, message=u'Variável não é falsa'):
        self.model = model
        self.key_field = key_field
        self.var_name = str(var_field).split('.')[-1]
        self.message = message

    def __call__(self, form, field):
        try:
            model_instance = self.model.query.filter(self.key_field == field.data).first()
        except:
            raise DatabaseAccessError()
        if model_instance and getattr(model_instance, self.var_name) is not False:
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
        if model_instance and getattr(model_instance, self.var_name) is not True:
            raise ValidationError(self.message)
