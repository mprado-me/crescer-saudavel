#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..data_providers.product import product_data_provider
from ..data_providers.products import products_data_provider

from flask import render_template, request


@app.route('/produto/<int:product_id>')
def product(product_id):
    data = product_data_provider.get_data(product_id)
    return render_template('products/product.html', data=data)


@app.route('/produtos/pagina/<int:page>/ordenacao/<int:sort_method>')
def all_products(page, sort_method):
    data = products_data_provider.get_all_products_data(page=page, sort_method=sort_method)
    return render_template('products/products.html', data=data)


@app.route('/produtos/categoria/<int:category_id>/pagina/<int:page>/ordenacao/<int:sort_method>')
def products_by_category(category_id, page, sort_method):
    data = products_data_provider.get_products_data_by_category(
        category_id=category_id,
        page=page,
        sort_method=sort_method)
    return render_template('products/products.html', data=data)


@app.route('/produtos/categoria/<int:category_id>/subcategoria/<int:subcategory_id>/pagina/<int:page>/ordenacao/<int:sort_method>')
def products_by_category_and_subcategory(category_id, subcategory_id, page, sort_method):
    data = products_data_provider.get_products_data_by_category_and_subcategory(
        category_id=category_id,
        subcategory_id=subcategory_id,
        page=page,
        sort_method=sort_method)
    return render_template('products/products.html', data=data)


@app.route('/produtos/busca/pagina/<int:page>')
def products_by_search(page):
    # Getting optional parameters
    q = request.args.get("q")

    # Setting default value to optional parameters
    if not q:
        q = ""

    data = products_data_provider.get_products_data_by_search(page=page, q=q)
    return render_template('products/products.html', data=data)
