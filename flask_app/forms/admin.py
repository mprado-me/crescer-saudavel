#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.admin.images.images import images_data_provider

from flask_app.forms.error_msg_provider import error_msg_provider
from flask_app.forms.widgets import personalized_textarea

from flask_app.models.category import Category

from flask_app.utils.form_field_validators import AllowedFileFormat, HasFilePart, Length, NotNegativeIntegerString, Price, Markdown

from flask_wtf import FlaskForm

from wtforms import FileField, StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange


class SimpleSubmitForm(FlaskForm):
    submit = SubmitField()


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


class CategoryFilterForm(FlaskForm):
    active = SelectField(
        label="Status da categoria",
        choices=[("True", "Ativa"), ("False", "Inativa")],
        validators=[
            DataRequired(message=error_msg_provider.data_required())
        ])
    filter = SubmitField(label="Filtrar")
# Category -- end --

# Subcategory -- begin --
class SubcategoryForm(FlaskForm):
    category_id = SelectField(label="Categoria", coerce=int, validators=[
        DataRequired(error_msg_provider.data_required())
    ])
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


class FilterSubcategoryForm(FlaskForm):
    category_id = SelectField(label="Categoria", coerce=int, validators=[
        DataRequired(error_msg_provider.data_required())
    ])
    active = SelectField(
        label="Status da categoria",
        choices=[("True", "Ativa"), ("False", "Inativa")],
        validators=[
            DataRequired(message=error_msg_provider.data_required())
        ])
    filter = SubmitField(label="Filtrar")

    def add_category_choices(self):
        add_category_choices(self, include_all_category=True)
# Subcategory -- end --

# Product -- begin --
class ProductForm(FlaskForm):
    title = StringField(
        label="Título",
        render_kw={
            "placeholder": "Ex.: Papinha de Maça - 300g",
            "size": "25"
        },
        validators=[
            DataRequired(message=error_msg_provider.data_required()),
            Length(max_length=128, message=error_msg_provider.product_title_length())
        ])
    category_subcategory = SelectField(
        label="Categoria/Subcategoria",
        choices=[("0", "0")],
        validators=[
            DataRequired(message=error_msg_provider.data_required())
        ])
    price = StringField(
        label="Preço em R$",
        render_kw={
            "placeholder": "Ex.: 8,80",
            "size": "12"
        },
        validators=[
            DataRequired(message=error_msg_provider.data_required()),
            Price(message=error_msg_provider.price()),
        ])
    stock_quantity = StringField(
        label="Quantidade no estoque",
        render_kw={
            "placeholder": "Ex.: 27",
            "size": "12"},
        validators=[
            DataRequired(message=error_msg_provider.data_required()),
            NotNegativeIntegerString(message=error_msg_provider.stock_quantity()),
        ])
    stop_sell_stock_quantity = StringField(
        label="Parar de vender quando o estoque estiver abaixo de",
        render_kw={
            "placeholder": "Ex.: 5",
            "size": "12"},
        validators=[
            DataRequired(message=error_msg_provider.data_required()),
            NotNegativeIntegerString(message=error_msg_provider.stock_quantity()),
        ])
    summary = TextAreaField(
        label="Resumo",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
            "example":
            """
                Lorem ipsum 'dolor' sit "amet", consectetur adipiscing elit. Nam fringilla augue nec est tristique auctor. Donec non est at libero vulputate rutrum. Morbi ornare lectus quis justo gravida semper. Nulla tellus mi, vulputate adipiscing cursus eu, suscipit id nulla. Donec a neque libero. Pellentesque aliquet, sem eget laoreet ultrices, ipsum metus feugiat sem, quis fermentum turpis eros eget velit. Donec ac tempus ante. Fusce ultricies massa massa. Fusce aliquam, purus eget sagittis vulputate.
            """
        },
        validators=[
            DataRequired(message=error_msg_provider.data_required()),
            Markdown(message=error_msg_provider.markdown_format())
        ])

    image_1 = SelectField(
        label="1º Imagem",
        choices=[("0", "0")],
        validators=[
            DataRequired(message=error_msg_provider.data_required())
        ])
    image_2 = SelectField(
        label="2º Imagem",
        choices=[("0", "0")],
        validators = [
        ])
    image_3 = SelectField(
        label="3º Imagem",
        choices=[("0", "0")],
        validators=[
        ])
    image_4 = SelectField(
        label="4º Imagem",
        choices=[("0", "0")],
        validators=[
        ])
    image_5 = SelectField(
        label="5º Imagem",
        choices=[("0", "0")],
        validators=[
        ])
    image_6 = SelectField(
        label="6º Imagem",
        choices=[("0", "0")],
        validators=[
        ])
    image_7 = SelectField(
        label="7º Imagem",
        choices=[("0", "0")],
        validators=[
        ])
    image_8 = SelectField(
        label="8º Imagem",
        choices=[("0", "0")],
        validators=[
        ])
    image_9 = SelectField(
        label="9º Imagem",
        choices=[("0", "0")],
        validators=[
        ])
    image_10 = SelectField(
        label="10º Imagem",
        choices=[("0", "0")],
        validators=[
        ])


    tab_1_title = StringField(
        label="Título da 1º aba",
        render_kw={
            "placeholder": "Ex.: Detalhes"
        },
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_1_content = TextAreaField(
        label="Conteúdo da 1º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
            "example":
            """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam fringilla augue nec est tristique auctor. Donec non est at libero vulputate rutrum. Morbi ornare lectus quis justo gravida semper. Nulla tellus mi, vulputate adipiscing cursus eu, suscipit id nulla. Donec a neque libero. Pellentesque aliquet, sem eget laoreet ultrices, ipsum metus feugiat sem, quis fermentum turpis eros eget velit. Donec ac tempus ante. Fusce ultricies massa massa. Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in accumsan elit odio quis mi. Cras neque metus, consequat et blandit et, luctus a nunc. Etiam gravida vehicula tellus, in imperdiet ligula euismod eget. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam erat mi, rutrum at sollicitudin rhoncus, ultricies posuere erat. Duis convallis, arcu nec aliquam consequat, purus felis vehicula felis, a dapibus enim lorem nec augue.
                <br>
                <br>
                Nunc facilisis sagittis ullamcorper. Proin lectus ipsum, gravida et mattis vulputate, tristique ut lectus. Sed et lorem nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aenean eleifend laoreet congue. Vivamus adipiscing nisl ut dolor dignissim semper. Nulla luctus malesuada tincidunt. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Integer enim purus, posuere at ultricies eu, placerat a felis. Suspendisse aliquet urna pretium eros convallis interdum. Quisque in arcu id dui vulputate mollis eget non arcu. Aenean et nulla purus. Mauris vel tellus non nunc mattis lobortis.
            """
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_2_title = StringField(
        label="Título da 2º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_2_content = TextAreaField(
        label="Conteúdo da 2º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_3_title = StringField(
        label="Título da 3º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_3_content = TextAreaField(
        label="Conteúdo da 3º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_4_title = StringField(
        label="Título da 4º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_4_content = TextAreaField(
        label="Conteúdo da 4º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_5_title = StringField(
        label="Título da 5º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_5_content = TextAreaField(
        label="Conteúdo da 5º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_6_title = StringField(
        label="Título da 6º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_6_content = TextAreaField(
        label="Conteúdo da 6º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_7_title = StringField(
        label="Título da 7º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_7_content = TextAreaField(
        label="Conteúdo da 7º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_8_title = StringField(
        label="Título da 8º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_8_content = TextAreaField(
        label="Conteúdo da 8º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_9_title = StringField(
        label="Título da 9º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_9_content = TextAreaField(
        label="Conteúdo da 9º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])
    tab_10_title = StringField(
        label="Título da 10º aba",
        validators=[
            Length(min_length=0, max_length=32, message=error_msg_provider.tab_title_length())
        ])
    tab_10_content = TextAreaField(
        label="Conteúdo da 10º aba",
        widget=personalized_textarea,
        render_kw={
            "markdown": True,
        },
        validators=[
            Markdown(message=error_msg_provider.markdown_format()),
        ])

    def add_choices(self):
        choices = [("0/0", "Nenhuma")]
        choices = choices + get_registered_category_subcategory_choices(self)
        self.category_subcategory.choices = choices[:]

        choices = []
        all_images_name = images_data_provider.get_images_name_sorted()
        for image_name in all_images_name:
            choices.append((image_name, image_name))
        self.image_1.choices = choices[:]

        choices.insert(0, ("", "Nenhuma"))

        self.image_2.choices = choices
        self.image_3.choices = choices
        self.image_4.choices = choices
        self.image_5.choices = choices
        self.image_6.choices = choices
        self.image_7.choices = choices
        self.image_8.choices = choices
        self.image_9.choices = choices
        self.image_10.choices = choices


class AddProductForm(ProductForm):
    add = SubmitField(label="Adicionar")

class EditProductForm(ProductForm):
    edit = SubmitField(label="Editar")

class FilterProductForm(FlaskForm):
    category_subcategory = SelectField(
        label="Categoria / Subcategoria",
        choices=[("0", "0")],
        validators=[
            DataRequired(message=error_msg_provider.data_required())
        ])
    active = SelectField(
        label="Status do produto",
        choices=[("True", "Ativo"), ("False", "Inativo")],
        validators=[
            DataRequired(message=error_msg_provider.data_required())
        ])
    filter = SubmitField(label="Filtrar")

    def add_category_subcategory_choices(self):
        choices = [("0 / 0", "Todas")]
        choices = choices + get_registered_category_subcategory_choices(self)
        self.category_subcategory.choices = choices[:]

class StockOperationForm(SimpleSubmitForm):
    amount = StringField(
        render_kw={
            "placeholder": "Ex.: 3",
            "size": "4"},
        validators=[
            DataRequired(message=error_msg_provider.data_required()),
            NotNegativeIntegerString(message=error_msg_provider.stock_quantity()),
        ])
# Product -- end --


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

def get_registered_category_subcategory_choices(form):
    choices = []
    categories = Category.query.order_by(Category.name).all()

    for category in categories:
        choices.append((str(category.id) + " / 0", category.name))
        for subcategory in category.subcategories:
            choices.append((str(category.id) + " / " + str(subcategory.id), category.name + " / " + subcategory.name))

    return choices