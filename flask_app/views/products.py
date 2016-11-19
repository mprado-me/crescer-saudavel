#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, render_template, request
from flask_app.data_providers.customer.products.product import product_data_provider

from flask_app.data_providers.customer.products.products import products_data_provider
from .. import app
from ..utils.decorators import log_route
from ..utils.exceptions import log_unrecognized_exception


@app.route('/produto/<int:product_id>')
@log_route
def product(product_id):
    try:
        data = product_data_provider.get_data(product_id)
        return render_template('products/product.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/produtos/pagina/<int:page>/ordenacao/<int:sort_method>')
@log_route
def all_products(page, sort_method):
    try:
        data = products_data_provider.get_all_products_data(page=page, sort_method=sort_method)
        return render_template('products/products.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/produtos/categoria/<int:category_id>/pagina/<int:page>/ordenacao/<int:sort_method>')
@log_route
def products_by_category(category_id, page, sort_method):
    try:
        data = products_data_provider.get_products_data_by_category(
            category_id=category_id,
            page=page,
            sort_method=sort_method)
        return render_template('products/products.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/produtos/categoria/<int:category_id>/subcategoria/<int:subcategory_id>/pagina/<int:page>/ordenacao/<int:sort_method>')
@log_route
def products_by_category_and_subcategory(category_id, subcategory_id, page, sort_method):
    try:
        data = products_data_provider.get_products_data_by_category_and_subcategory(
            category_id=category_id,
            subcategory_id=subcategory_id,
            page=page,
            sort_method=sort_method)
        return render_template('products/products.html', data=data)
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
        return render_template('products/products.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
