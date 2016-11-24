#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast

from decimal import Decimal

from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import login_required

from flask_app import app

from flask_app.data_providers.admin.products.categories import categories_data_provider
from flask_app.data_providers.admin.products.products import products_data_provider
from flask_app.data_providers.admin.products.subcategories import subcategories_data_provider

from flask_app.forms.admin import StockOperationForm, AddSubcategoryForm, AddCategoryForm, AddProductForm, EditSubcategoryForm, EditCategoryForm, EditProductForm, FilterProductForm, FilterCategoryForm, SimpleSubmitForm

from flask_app.models.category import Category
from flask_app.models.product import Product
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

            category_id = int(form.category_subcategory.data.split('/')[0])
            if category_id == 0:
                category_id = None
            subcategory_id = int(form.category_subcategory.data.split('/')[1])
            if subcategory_id == 0:
                subcategory_id = None

            product = Product(
                title=form.title.data,
                category_id=category_id,
                subcategory_id=subcategory_id,
                price=Decimal(form.price.data.replace(',', '.')),
                stock_quantity=int(form.stock_quantity.data),
                stop_sell_stock_quantity=int(form.stop_sell_stock_quantity.data),
                summary=form.summary.data,

                image_1=form.image_1.data,
                image_2=form.image_2.data,
                image_3=form.image_3.data,
                image_4=form.image_4.data,
                image_5=form.image_5.data,
                image_6=form.image_6.data,
                image_7=form.image_7.data,
                image_8=form.image_8.data,
                image_9=form.image_9.data,
                image_10=form.image_10.data,

                tab_1_title=form.tab_1_title.data,
                tab_1_content=form.tab_1_content.data,
                tab_2_title=form.tab_2_title.data,
                tab_2_content=form.tab_2_content.data,
                tab_3_title=form.tab_3_title.data,
                tab_3_content=form.tab_3_content.data,
                tab_4_title=form.tab_4_title.data,
                tab_4_content=form.tab_4_content.data,
                tab_5_title=form.tab_5_title.data,
                tab_5_content=form.tab_5_content.data,
                tab_6_title=form.tab_6_title.data,
                tab_6_content=form.tab_6_content.data,
                tab_7_title=form.tab_7_title.data,
                tab_7_content=form.tab_7_content.data,
                tab_8_title=form.tab_8_title.data,
                tab_8_content=form.tab_8_content.data,
                tab_9_title=form.tab_9_title.data,
                tab_9_content=form.tab_9_content.data,
                tab_10_title=form.tab_10_title.data,
                tab_10_content=form.tab_10_content.data,
            )

            db_manager.add(product)
            db_manager.commit()

            db_manager.refresh(product)
            flash("Produto \"%s\" foi adicionado com sucesso. Clique <a target='_blank' href=%s>aqui</a> para ver o produto." % (form.title.data, url_for("product", product_id=product.id)), "success")
            return redirect(url_for("admin_add_product"))
        except Exception as e:
            db_manager.rollback()
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/editar-produto/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_edit_product(product_id):
    form = EditProductForm()

    # GET
    if request.method == "GET":
        try:
            product = db_manager.get_product(product_id)
            if not product:
                raise InvalidUrlParamError()

            form.add_choices()

            data = products_data_provider.get_edit_data(form=form, product_id=product_id)
            return render_template("admin/products/edit_product.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            product = db_manager.get_product(product_id)
            if not product:
                raise InvalidUrlParamError()

            form.add_choices()

            if not form.validate_on_submit():
                data = products_data_provider.get_edit_data(form=form, product_id=product_id)
                return render_template("admin/products/edit_product.html", data=data)

            category_id = int(form.category_subcategory.data.split('/')[0])
            if category_id == 0:
                category_id = None
            subcategory_id = int(form.category_subcategory.data.split('/')[1])
            if subcategory_id == 0:
                subcategory_id = None

            product.title=form.title.data,
            product.category_id=category_id,
            product.subcategory_id=subcategory_id,
            product.price=Decimal(form.price.data.replace(',', '.')),
            product.stock_quantity=int(form.stock_quantity.data),
            product.stop_sell_stock_quantity=int(form.stop_sell_stock_quantity.data)
            product.summary=form.summary.data,

            product.image_1=form.image_1.data,
            product.image_2=form.image_2.data,
            product.image_3=form.image_3.data,
            product.image_4=form.image_4.data,
            product.image_5=form.image_5.data,
            product.image_6=form.image_6.data,
            product.image_7=form.image_7.data,
            product.image_8=form.image_8.data,
            product.image_9=form.image_9.data,
            product.image_10=form.image_10.data,

            product.tab_1_title=form.tab_1_title.data,
            product.tab_1_content=form.tab_1_content.data,
            product.tab_2_title=form.tab_2_title.data,
            product.tab_2_content=form.tab_2_content.data,
            product.tab_3_title=form.tab_3_title.data,
            product.tab_3_content=form.tab_3_content.data,
            product.tab_4_title=form.tab_4_title.data,
            product.tab_4_content=form.tab_4_content.data,
            product.tab_5_title=form.tab_5_title.data,
            product.tab_5_content=form.tab_5_content.data,
            product.tab_6_title=form.tab_6_title.data,
            product.tab_6_content=form.tab_6_content.data,
            product.tab_7_title=form.tab_7_title.data,
            product.tab_7_content=form.tab_7_content.data,
            product.tab_8_title=form.tab_8_title.data,
            product.tab_8_content=form.tab_8_content.data,
            product.tab_9_title=form.tab_9_title.data,
            product.tab_9_content=form.tab_9_content.data,
            product.tab_10_title=form.tab_10_title.data,
            product.tab_10_content=form.tab_10_content.data,

            db_manager.add(product)
            db_manager.commit()

            flash(
                "Produto #%s \"%s\" foi editado com sucesso. Clique <a target='_blank' href=%s>aqui</a> para ver o produto." %
                (product.id, product.title, url_for("product", product_id=product.id)), "success")
            return redirect(url_for("admin_products", page=1))
        except Exception as e:
            db_manager.rollback()
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/produtos/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_products(page):
    filter_product_form = FilterProductForm()
    action_form = SimpleSubmitForm()
    stock_operation_form = StockOperationForm()

    # Getting optional parameters
    category_subcategory = request.args.get('category_subcategory')
    active = request.args.get('active')

    # Setting default value to optional parameters
    if not category_subcategory:
        category_subcategory = "0/0"
    if not active:
        active = "True"

    try:
        # Converting query parameters from string type to his respective python type
        category_id = int(category_subcategory.split('/')[0])
        if category_id == 0:
            category_id = None
        subcategory_id = int(category_subcategory.split('/')[1])
        if subcategory_id == 0:
            subcategory_id = None
        active = ast.literal_eval(active)

        filter_product_form.add_category_subcategory_choices()

        data = products_data_provider.get_data(
            page=page,
            action_form=action_form,
            stock_operation_form=stock_operation_form,
            filter_product_form=filter_product_form,
            category_id=category_id,
            subcategory_id=subcategory_id,
            active = active,
            category_subcategory=category_subcategory
        )
        return render_template("admin/products/products.html", data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-produto/<int:product_id>', methods=['POST'])
@login_required
@admin
@log_route
def admin_remove_product(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/reativar-produto/<int:product_id>', methods=['POST'])
@login_required
@admin
@log_route
def admin_reactivate_product(product_id):
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
            subcategory = db_manager.get_subcategory(subcategory_id)
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
            subcategory = db_manager.get_subcategory(subcategory_id)
            if not subcategory:
                raise InvalidUrlParamError()

            form.add_category_choices()

            if not form.validate_on_submit():
                data = subcategories_data_provider.get_edit_data(form, subcategory_id=subcategory_id)
                return render_template("admin/products/edit_subcategory.html", data=data)

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
