#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, render_template, request
from flask_app.data_providers.customer.products.product import product_data_provider

from flask_app.data_providers.customer.products.products import products_data_provider
from flask_app import app
from flask_app.utils.decorators import log_route
from flask_app.utils.exceptions import InvalidQueryArgError, log_unrecognized_exception
from flask_app.utils.query_params_validators import ValidCategoryIdSubcategoryId


@app.route('/produto/<int:product_id>')
@log_route
def product(product_id):
    try:
        data = product_data_provider.get_data(product_id)
        return render_template('customer/products/product.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/produtos/pagina/<int:page>/ordenacao/<int:sort_method>')
@log_route
def products(page, sort_method):
    try:
        # Getting query params
        category_id = request.args.get("category_id")
        subcategory_id = request.args.get("subcategory_id")

        # Validating query params
        ValidCategoryIdSubcategoryId(category_id=category_id, subcategory_id=subcategory_id).__call__()

        data = products_data_provider.get_products_data(
            page=page,
            sort_method=sort_method,
            category_id=category_id,
            subcategory_id=subcategory_id)
        return render_template('customer/products/products.html', data=data)
    except InvalidQueryArgError:
        abort(404)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/produtos/busca/pagina/<int:page>')
@log_route
def products_by_search(page):
    try:
        # Getting optional parameters
        q = request.args.get("q")

        # Setting default value to optional parameters
        if not q:
            q = ""

        data = products_data_provider.get_products_data_by_search(page=page, q=q)
        return render_template('customer/products/products.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
