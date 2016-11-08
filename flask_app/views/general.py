#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..data_providers.about_us import AboutUsDataProvider
from ..data_providers.checkout import CheckoutDataProvider
from ..data_providers.faq import FaqDataProvider
from ..data_providers.home import HomeDataProvider
from ..data_providers.my_account import MyAccountDataProvider
from ..data_providers.order import OrderDataProvider

from flask import abort, redirect, render_template, request, url_for, session
from flask_login import login_required


@app.route('/sobre-nos')
def about_us():
    data = AboutUsDataProvider().get_data()
    return render_template('general/about-us.html', data=data)


@app.route('/finalizacao-de-compra/passo/<int:step>')
@login_required
def checkout(step):
    user_email = session["user_id"]
    in_edit_info_mode = request.args.get("editar")
    if in_edit_info_mode and in_edit_info_mode == "sim":
        in_edit_info_mode = True
    else:
        in_edit_info_mode = False
    data = CheckoutDataProvider().get_data(step, in_edit_info_mode, user_email=user_email)
    return render_template('general/checkout.html', data=data)


@app.route('/faq')
def faq():
    data = FaqDataProvider().get_data()
    return render_template('general/faq.html', data=data)


@app.route('/')
@app.route('/home')
def home():
    data = HomeDataProvider().get_data()
    return render_template('general/home.html', data=data)


@app.route('/minha-conta', methods=['GET', 'POST'])
@login_required
def my_account():
    if request.method == 'GET':
        editable = request.args.get("editar")
        if editable and editable == "sim":
            editable = True
        else:
            editable = False
        data = MyAccountDataProvider().get_data(editable)
        return render_template('general/my-account.html', data=data)
    elif request.method == 'POST':
        # TODO: Deal with post
        return redirect(url_for('my_account'))
    abort(404)


@app.route('/pedido/<int:order_id>')
@login_required
def order(order_id):
    data = OrderDataProvider().get_data(order_id)
    return render_template('general/order.html', data=data)
