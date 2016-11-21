#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.forms.error_msg_provider import error_msg_provider

from flask_app.utils.form_field_validators import AllowedFileFormat, HasFilePart, Length

from flask_wtf import FlaskForm

from wtforms import FileField, StringField, SubmitField
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    category = StringField(label="Nome da categoria", validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Length(max_length=64, message=error_msg_provider.category_too_long())])


class AddCategoryForm(CategoryForm):
    add = SubmitField(label="Adicionar")


class EditCategoryForm(CategoryForm):
    edit = SubmitField(label="Editar")


class SimpleSubmitForm(FlaskForm):
    submit = SubmitField()


class UploadImageForm(FlaskForm):
    allowed_extensions = ["png", "jpg", "jpeg"]
    image = FileField('Image', validators=[
        HasFilePart(input_file_name="file", message=error_msg_provider.none_file_selected_msg(), stop=True),
        AllowedFileFormat(
            input_file_name="file",
            allowed_extensions=allowed_extensions,
            message=error_msg_provider.invalid_file_format_msg(allowed_extensions=allowed_extensions)
        )]
    )
