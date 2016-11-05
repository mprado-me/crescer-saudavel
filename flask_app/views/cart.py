#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect

from flask_app import app

from ..data_providers.cart import CartDataProvider

@app.route('/carrinho')
def cart():
    data = CartDataProvider().get_data()
    return render_template('cart/cart.html', cart_table_editable=True, data=data)

@app.route('/adicionar-ao-carrinho/produto/<int:product_id>/quantidade/<int:quantity>', methods=['POST'])
def cart_add_product(product_id, quantity):
    return redirect(url_for('cart'))

@app.route('/remover-do-carrinho/produto/<int:product_id>/quantidade/<int:quantity>', methods=['POST'])
def cart_remove_product(product_id, quantity):
    return redirect(url_for('cart'))

@app.route('/deletar-do-carrinho/produto/<int:product_id>', methods=['POST'])
def cart_delete_product(product_id):
    return redirect(url_for('cart'))

@app.route('/deletar-tudo-do-carrinho', methods=['POST'])
def cart_delete_all_products():
    return redirect(url_for('cart'))