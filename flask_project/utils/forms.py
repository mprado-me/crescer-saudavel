#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

data_required_msg = "Campo obrigatório"
email_invalid_format_msg = "Formato do email inválido"
password_length_msg = "A senha deve possuir entre 6 e 32 caracteres"
password_mismatch_msg = "As senhas digitadas não são iguais"

class CreateAccountForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message=data_required_msg), Email(message=email_invalid_format_msg)])
    password = PasswordField('Senha', validators=[DataRequired(message=data_required_msg), Length(min=6, max=32, message=password_length_msg), EqualTo('password_confirmation', message=password_mismatch_msg)])
    password_confirmation = PasswordField('Confirmação de senha', validators=[DataRequired(message=data_required_msg)])