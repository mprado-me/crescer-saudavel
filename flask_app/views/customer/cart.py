#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, redirect, render_template, session, url_for
from flask_login import login_required

from flask_app.data_providers.customer.cart.cart import cart_data_provider
from flask_app import app
from flask_app.utils.decorators import log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/carrinho')
@login_required
@log_route
def cart():
    try:
        # Getting user session identifier. Aka user_email
        user_email = session["user_id"]

        data = cart_data_provider.get_data(user_email=user_email)
        return render_template('customer/cart/cart.html', cart_table_editable=True, data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)

@app.route('/adicionar-ao-carrinho/produto/<int:product_id>/quantidade/<int:quantity>', methods=['POST'])
@login_required
@log_route
def cart_add_product(product_id, quantity):
    try:
        # TODO: Implement
        return redirect(url_for('cart'))
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/remover-do-carrinho/produto/<int:product_id>/quantidade/<int:quantity>', methods=['POST'])
@login_required
@log_route
def cart_remove_product(product_id, quantity):
    try:
        # TODO: Implement
        return redirect(url_for('cart'))
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/deletar-do-carrinho/produto/<int:product_id>', methods=['POST'])
@login_required
@log_route
def cart_delete_product(product_id):
    try:
        # TODO: Implement
        return redirect(url_for('cart'))
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/deletar-tudo-do-carrinho', methods=['POST'])
@login_required
@log_route
def cart_delete_all_products():
    try:
        # TODO: Implement
        return redirect(url_for('cart'))
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
