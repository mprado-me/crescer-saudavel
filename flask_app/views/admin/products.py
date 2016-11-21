#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, redirect, render_template, request, url_for
from flask_login import login_required

from flask_app import app

from flask_app.data_providers.admin.products.categories import categories_data_provider

from flask_app.forms.admin import AddCategoryForm, EditCategoryForm, SimpleSubmitForm

from flask_app.models.category import Category

from flask_app.utils.db_manager import db_manager
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import DatabaseAccessError, InvalidUrlParamError, log_unrecognized_exception


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
            return render_template("admin/products/add_category.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = categories_data_provider.get_add_data(form=form)
                return render_template("admin/products/add_category.html", data=data)

            category = Category(
                name=form.category.data
            )
            db_manager.add_category(category)
            db_manager.commit()

            return redirect(url_for("admin_add_product_category",
                                    msg_content="Categoria %s foi adicionada com sucesso." % form.category.data,
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

    # Getting optional parameters
    page_to_return = request.args.get('page_to_return')

    # Setting default value to optional parameters
    if not page_to_return:
        page_to_return = 1

    # GET
    if request.method == "GET":
        try:
            data = categories_data_provider.get_edit_data(form=form, category_id=category_id, page_to_return=page_to_return)
            return render_template("admin/products/edit_category.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = categories_data_provider.get_edit_data(form=form, category_id=category_id, page_to_return=page_to_return)
                return render_template("admin/products/edit_category.html", data=data)

            category = db_manager.get_category(category_id=category_id)

            if not category:
                raise InvalidUrlParamError("Category not found")

            category.name = form.category.data
            db_manager.add_category(category)
            db_manager.commit()

            return redirect(url_for("admin_product_categories",
                                    page=page_to_return,
                                    msg_content="Categoria #%s foi editada com sucesso." % category.id,
                                    msg_type="success"))
        except DatabaseAccessError:
            db_manager.rollback()
            abort(500)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/remover-categoria-de-produto/<int:category_id>', methods=['POST'])
@login_required
@admin
@log_route
def admin_remove_product_category(category_id):
    remove_form = SimpleSubmitForm()

    # Getting optional parameters
    page_to_return = request.args.get('page_to_return')

    # Setting default value to optional parameters
    if not page_to_return:
        page_to_return = 1

    if not remove_form.validate_on_submit():
        return redirect(url_for("admin_product_categories",
                                page=page_to_return,
                                msg_content="Não foi possível remover a categoria #%s. Tente novamente." % category_id,
                                msg_type="warning"))

    try:
        category = db_manager.get_category(category_id=category_id)

        if not category:
            raise InvalidUrlParamError("Category not found")

        db_manager.delete_category(category)
        db_manager.commit()

        return redirect(url_for("admin_product_categories",
                                page=page_to_return,
                                msg_content="Categoria #%s (%s) foi removida com sucesso." % (category.id, category.name),
                                msg_type="success"))
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/categorias-de-produto/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_product_categories(page):
    remove_form = SimpleSubmitForm()

    try:
        data = categories_data_provider.get_data(page=page, remove_form=remove_form)
        return render_template("admin/products/categories.html", data=data)
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
