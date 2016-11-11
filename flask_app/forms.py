#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models.user import User

from .utils.validators import NotUnique, Unique, VariableTrue

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length

data_required_msg = "Campo obrigatório"
email_already_registered_msg = "Email já cadastrado"
email_invalid_format_msg = "Formato de email inválido"
email_not_registered_msg = "Email não cadastrado"
password_length_msg = "A senha deve possuir entre 6 e 32 caracteres"
password_mismatch_msg = "As senhas digitadas não são iguais"
unconfirmed_email_msg = "Email não confirmado"


class CreateAccountForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message=data_required_msg),
        Email(message=email_invalid_format_msg),
        Unique(model=User, field=User.email, message=email_already_registered_msg)])
    password = PasswordField('Senha', validators=[
        DataRequired(message=data_required_msg),
        Length(min=6, max=32, message=password_length_msg),
        EqualTo('password_confirmation', message=password_mismatch_msg)])
    password_confirmation = PasswordField('Confirmação de senha', validators=[
        DataRequired(message=data_required_msg)])


class RecoverPasswordForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message=data_required_msg),
        Email(message=email_invalid_format_msg),
        NotUnique(model=User, field=User.email, message=email_not_registered_msg),
        VariableTrue(model=User, key_field=User.email, var_field=User.email_confirmed, message=unconfirmed_email_msg)])


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message=data_required_msg),
        Email(message=email_invalid_format_msg)])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message=data_required_msg),
        Email(message=email_invalid_format_msg)])
    password = PasswordField('Senha', validators=[
        DataRequired(message=data_required_msg),
        Length(min=6, max=32, message=password_length_msg)])


class RedefinePasswordForm(FlaskForm):
    password = PasswordField('Senha', validators=[
        DataRequired(message=data_required_msg),
        Length(min=6, max=32, message=password_length_msg),
        EqualTo('password_confirmation', message=password_mismatch_msg)])
    password_confirmation = PasswordField('Confirmação de senha', validators=[
        DataRequired(message=data_required_msg)])
