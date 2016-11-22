#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.forms.error_msg_provider import error_msg_provider

from flask_app.models.category import Category

from flask_app.utils.form_field_validators import AllowedFileFormat, Contains, HasFilePart, Length

from flask_wtf import FlaskForm

from wtforms import FileField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

# Category -- begin
class CategoryForm(FlaskForm):
    category = StringField(label="Nome da categoria", validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Length(max_length=64, message=error_msg_provider.category_too_long())
    ])


class AddCategoryForm(CategoryForm):
    add = SubmitField(label="Adicionar")


class EditCategoryForm(CategoryForm):
    edit = SubmitField(label="Editar")
# Category -- end --

# Subcategory -- begin --
class SubcategoryForm(FlaskForm):
    category_id = SelectField(label="Categoria", coerce=int)
    subcategory = StringField(label="Nome da subcategoria", validators=[
        DataRequired(message=error_msg_provider.data_required()),
        Length(max_length=64, message=error_msg_provider.subcategory_too_long())
    ])

    def add_category_choices(self):
        add_category_choices(self, include_all_category=False)


class AddSubcategoryForm(SubcategoryForm):
    add = SubmitField(label="Adicionar")


class EditSubcategoryForm(SubcategoryForm):
    edit = SubmitField(label="Editar")


class FilterCategoryForm(FlaskForm):
    category_id = SelectField(label="Categoria", coerce=int)
    filter = SubmitField(label="Filtrar")

    def add_category_choices(self):
        add_category_choices(self, include_all_category=True)
# Subcategory -- end --

# Product -- begin --
class ProductForm(FlaskForm):
    pass

class AddProductForm(ProductForm):
    pass

class EditProductForm(ProductForm):
    pass
# Product -- end --

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
        )
    ])
    upload = SubmitField(label="Upload")


def add_category_choices(form, include_all_category=False):
    categories = Category.query.order_by(Category.name).all()
    form.category_id.choices = [(category.id, category.name) for category in categories]
    if include_all_category:
        form.category_id.choices.insert(0, (0, "Todas"))