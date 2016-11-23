#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import login_required

from flask_app import app

from flask_app.data_providers.admin.products.categories import categories_data_provider
from flask_app.data_providers.admin.products.products import products_data_provider
from flask_app.data_providers.admin.products.subcategories import subcategories_data_provider

from flask_app.forms.admin import AddSubcategoryForm, AddCategoryForm, AddProductForm, EditSubcategoryForm, EditCategoryForm, FilterCategoryForm, SimpleSubmitForm

from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory

from flask_app.utils.db_manager import db_manager
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import DatabaseAccessError, InsecurePostException, InvalidQueryParamError, InvalidUrlParamError, log_unrecognized_exception


@app.route('/painel-administrativo/adicionar-produto', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_product():
    form = AddProductForm()

    # GET
    if request.method == "GET":
        try:
            form.add_choices()

            data = products_data_provider.get_add_data(form = form)
            return render_template("admin/products/add_product.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            form.add_choices()

            if not form.validate_on_submit():
                data = products_data_provider.get_add_data(form=form)
                return render_template("admin/products/add_product.html", data=data)

            return "Produto adicionado com sucesso"
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
            db_manager.add(category)
            db_manager.commit()

            flash("Categoria \"%s\" foi adicionada com sucesso." % form.category.data, "success")
            return redirect(url_for("admin_add_product_category"))
        except DatabaseAccessError:
            db_manager.rollback()
            abort(500)
        except Exception as e:
            db_manager.rollback()
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
            db_manager.add(category)
            db_manager.commit()

            flash("Categoria #%s foi editada com sucesso." % category.id, "success")
            return redirect(url_for("admin_product_categories", page=page_to_return))
        except DatabaseAccessError:
            db_manager.rollback()
            abort(500)
        except Exception as e:
            db_manager.rollback()
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

    try:
        if not remove_form.validate_on_submit():
            raise InsecurePostException()

        category = db_manager.get_category(category_id=category_id)

        if not category:
            raise InvalidUrlParamError("Category not found")

        db_manager.delete(category)
        db_manager.commit()

        flash("Categoria #%s \"%s\" foi removida com sucesso." % (category.id, category.name), "success")
        return redirect(url_for("admin_product_categories", page=page_to_return))
    except DatabaseAccessError:
        db_manager.rollback()
        abort(500)
    except Exception as e:
        db_manager.rollback()
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
    form = AddSubcategoryForm()

    # GET
    if request.method == "GET":
        try:
            form.add_category_choices()

            data = subcategories_data_provider.get_add_data(form)
            return render_template("admin/products/add_subcategory.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            form.add_category_choices()

            if not form.validate_on_submit():
                data = subcategories_data_provider.get_add_data(form)
                return render_template("admin/products/add_subcategory.html", data=data)

            subcategory = Subcategory(
                category_id=form.category_id.data,
                name=form.subcategory.data
            )
            db_manager.add(subcategory)
            db_manager.commit()

            flash("Subcategoria \"%s\" foi adicionada com sucesso." % form.subcategory.data, "success")
            return redirect(url_for("admin_add_product_subcategory"))
        except DatabaseAccessError:
            db_manager.rollback()
            abort(500)
        except Exception as e:
            db_manager.rollback()
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/editar-subcategoria-de-produto/<int:subcategory_id>', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_edit_product_subcategory(subcategory_id):
    form = EditSubcategoryForm()

    # GET
    if request.method == "GET":
        try:
            subcategory = Subcategory.query.filter(Subcategory.id == subcategory_id).one_or_none()
            if not subcategory:
                raise InvalidUrlParamError()

            form.add_category_choices()

            data = subcategories_data_provider.get_edit_data(form, subcategory_id=subcategory_id)
            return render_template("admin/products/edit_subcategory.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            form.add_category_choices()

            if not form.validate_on_submit():
                data = subcategories_data_provider.get_edit_data(form, subcategory_id=subcategory_id)
                return render_template("admin/products/edit_subcategory.html", data=data)

            subcategory = db_manager.get_subcategory(subcategory_id)
            subcategory.name = form.subcategory.data
            subcategory.category_id = form.category_id.data
            db_manager.add(subcategory)
            db_manager.commit()

            flash("Subcategoria #%s foi editada com sucesso." % subcategory_id, "success")
            return redirect(url_for("admin_product_subcategories", page=1))
        except DatabaseAccessError:
            db_manager.rollback()
            abort(500)
        except Exception as e:
            db_manager.rollback()
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/remover-subcategoria-de-produto/<int:subcategory_id>', methods=['POST'])
@login_required
@admin
@log_route
def admin_remove_product_subcategory(subcategory_id):
    remove_form = SimpleSubmitForm()

    try:
        if not remove_form.validate_on_submit():
            raise InsecurePostException()

        subcategory = db_manager.get_subcategory(subcategory_id=subcategory_id)

        if not subcategory:
            raise InvalidUrlParamError("Subcategory not found")

        db_manager.delete(subcategory)
        db_manager.commit()

        flash("Subcategoria #%s \"%s\" foi removida com sucesso." % (subcategory.id, subcategory.name), "success")
        return redirect(url_for("admin_product_subcategories", page=1))
    except DatabaseAccessError:
        db_manager.rollback()
        abort(500)
    except Exception as e:
        db_manager.rollback()
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/subcategorias-de-produto/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_product_subcategories(page):
    filter_category_form = FilterCategoryForm()
    remove_form = SimpleSubmitForm()

    # Getting optional parameters
    category_id = request.args.get('category_id')

    # Setting default value to optional parameters
    try:
        category_id_as_int = int(category_id)
        if category_id_as_int <= 0:
            raise InvalidQueryParamError()
    except Exception:
        category_id = None

    try:
        filter_category_form.add_category_choices()

        data = subcategories_data_provider.get_data(
            page=page,
            remove_form=remove_form,
            filter_category_form=filter_category_form,
            category_id=category_id)
        return render_template("admin/products/subcategories.html", data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
