#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..data_providers.cart import CartDataProvider

from flask import redirect, render_template, session, url_for
from flask_login import login_required


@app.route('/carrinho')
@login_required
def cart():
    user_email = session["user_id"]
    data = CartDataProvider().get_data(user_email=user_email)
    return render_template('cart/cart.html', cart_table_editable=True, data=data)


@app.route('/adicionar-ao-carrinho/produto/<int:product_id>/quantidade/<int:quantity>', methods=['POST'])
@login_required
def cart_add_product(product_id, quantity):
    return redirect(url_for('cart'))


@app.route('/remover-do-carrinho/produto/<int:product_id>/quantidade/<int:quantity>', methods=['POST'])
@login_required
def cart_remove_product(product_id, quantity):
    return redirect(url_for('cart'))


@app.route('/deletar-do-carrinho/produto/<int:product_id>', methods=['POST'])
@login_required
def cart_delete_product(product_id):
    return redirect(url_for('cart'))


@app.route('/deletar-tudo-do-carrinho', methods=['POST'])
@login_required
def cart_delete_all_products():
    return redirect(url_for('cart'))
