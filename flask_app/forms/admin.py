#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.forms.error_msg_provider import error_msg_provider

from flask_app.utils.form_field_validators import AllowedFileFormat, HasFilePart, Length

from flask_wtf import FlaskForm

from wtforms import FileField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

# Category
class CategoryForm(FlaskForm):
    category = StringField(label="Nome da categoria", validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Length(max_length=64, message=error_msg_provider.category_too_long())])


class AddCategoryForm(CategoryForm):
    add = SubmitField(label="Adicionar")


class EditCategoryForm(CategoryForm):
    edit = SubmitField(label="Editar")


# Subcategory
class SubcategoryForm(FlaskForm):
    category = SelectField(label="Categoria", coerce=int)
    subcategory = StringField(label="Nome da subcategoria", validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Length(max_length=64, message=error_msg_provider.subcategory_too_long())])

    def add_category_choices(self):
        # TODO: Get categories from db
        self.category.choices = [(1, "Categoria 1"), (2, "Categoria 2"), (3, "Categoria 3")]


class AddSubcategoryForm(SubcategoryForm):
    add = SubmitField(label="Adicionar")


class EditSubcategoryForm(SubcategoryForm):
    edit = SubmitField(label="Editar")


class SimpleSubmitForm(FlaskForm):
    submit = SubmitField()


class UploadImageForm(FlaskForm):
    allowed_extensions = ["png", "jpg", "jpeg"]
    image = FileField(label='Imagem', validators=[
        HasFilePart(input_file_name="image", message=error_msg_provider.none_file_selected_msg(), stop=True),
        AllowedFileFormat(
            input_file_name="image",
            allowed_extensions=allowed_extensions,
            message=error_msg_provider.invalid_file_format_msg(allowed_extensions=allowed_extensions)
        )]
    )
    upload = SubmitField(label="Upload")
