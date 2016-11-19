#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .error_msg_provider import error_msg_provider

from flask_app.models.user import User

from flask_app.utils.form_field_validators import CorrectPassword, Email, Length, NotUnique, Unique, VariableFalse, VariableTrue

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo


class CreateAccountForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Email(message=error_msg_provider.email_invalid_format(), stop=True),
        Unique(model=User, field=User.email, message=error_msg_provider.email_already_registered())])
    password = PasswordField('Senha', validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Length(min_length=6, max_length=32, message=error_msg_provider.password_length(), stop=True),
        EqualTo('password_confirmation', message=error_msg_provider.password_mismatch())])
    password_confirmation = PasswordField('Confirmação de senha', validators=[
        DataRequired(message=error_msg_provider.data_required())])


class RecoverPasswordForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Email(message=error_msg_provider.email_invalid_format(), stop=True),
        NotUnique(model=User, field=User.email, message=error_msg_provider.email_not_registered, stop=True),
        VariableTrue(model=User, key_field=User.email, var_field=User.email_confirmed, message=error_msg_provider.unconfirmed_email)])


class ResendConfirmationEmailForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Email(message=error_msg_provider.email_invalid_format(), stop=True),
        NotUnique(model=User, field=User.email, message=error_msg_provider.email_not_registered, stop=True),
        VariableFalse(model=User, key_field=User.email, var_field=User.email_confirmed, message=error_msg_provider.confirmed_email())])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Email(message=error_msg_provider.email_invalid_format(), stop=True),
        NotUnique(model=User, field=User.email, message=error_msg_provider.email_not_registered, stop=True),
        VariableTrue(model=User, key_field=User.email, var_field=User.email_confirmed, message=error_msg_provider.unconfirmed_email)])
    password = PasswordField('Senha', validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Length(min_length=6, max_length=32, message=error_msg_provider.password_length(), stop=True),
        CorrectPassword(message=error_msg_provider.incorrect_password())])


class RedefinePasswordForm(FlaskForm):
    password = PasswordField('Senha', validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Length(min_length=6, max_length=32, message=error_msg_provider.password_length(), stop=True),
        EqualTo('password_confirmation', message=error_msg_provider.password_mismatch())])
    password_confirmation = PasswordField('Confirmação de senha', validators=[
        DataRequired(message=error_msg_provider.data_required())])
