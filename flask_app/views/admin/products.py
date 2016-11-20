#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, redirect, render_template, request, url_for
from flask_login import login_required

from flask_app import app

from flask_app.data_providers.admin.products.categories import categories_data_provider

from flask_app.forms.admin import AddCategoryForm, EditCategoryForm

from flask_app.models.category import Category

from flask_app.utils.db_manager import db_manager
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import DatabaseAccessError, log_unrecognized_exception


@app.route('/painel-administrativo/adicionar-produto', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_product():
    form = None

    # GET
    if request.method == "GET":
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/editar-produto/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_edit_product(product_id):
    form = None

    # GET
    if request.method == "GET":
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/produtos/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_products(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/adicionar-ao-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_add_to_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-do-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_remove_from_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/atualizar-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_update_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/adicionar-categoria-de-produto', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_product_category():
    form = AddCategoryForm()

    # GET
    if request.method == "GET":
        try:
            data = categories_data_provider.get_add_data(form=form)
            return render_template("admin/products/add_edit_product_category.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = categories_data_provider.get_add_data(form=form)
                return render_template("admin/products/add_edit_product_category.html", data=data)

            category = Category(
                name=form.category.data
            )
            db_manager.add_category(category)
            db_manager.commit()

            return redirect(url_for("admin_add_product_category",
                                    msg_content="Categoria %s adicionada com sucesso." % form.category.data,
                                    msg_type="success"))
        except DatabaseAccessError:
            db_manager.rollback()
            abort(500)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/editar-categoria-de-produto/<int:category_id>', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_edit_product_category(category_id):
    form = EditCategoryForm()

    # GET
    if request.method == "GET":
        try:
            data = categories_data_provider.get_edit_data(form=form, category_id=category_id)
            return render_template("admin/products/add_edit_product_category.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/categorias-de-produto/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_product_categories(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/adicionar-subcategoria-de-produto', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_product_subcategory():
    form = None

    # GET
    if request.method == "GET":
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/editar-subcategoria-de-produto/<int:subcategory_id>', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_edit_product_subcategory(subcategory_id):
    form = None

    # GET
    if request.method == "GET":
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/subcategorias-de-produto/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_product_subcategories(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
