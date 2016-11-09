#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..data_providers.about_us import about_us_data_provider
from ..data_providers.checkout import checkout_data_provider
from ..data_providers.faq import faq_data_provider
from ..data_providers.home import home_data_provider
from ..data_providers.my_account import my_account_data_provider
from ..data_providers.order import order_data_provider

from ..utils.decorators import log_route

from flask import abort, redirect, render_template, request, url_for, session
from flask_login import login_required


@app.route('/sobre-nos')
@log_route
def about_us():
    data = about_us_data_provider.get_data()
    return render_template('general/about-us.html', data=data)


@app.route('/finalizacao-de-compra/passo/<int:step>')
@login_required
@log_route
def checkout(step):
    # Getting user session identifier. Aka user_email
    user_email = session["user_id"]

    # Getting optional parameters
    user_info_editable = request.args.get("editar")

    # Setting default value to optional parameters
    if step == 1 and user_info_editable and user_info_editable == "sim":
        user_info_editable = True
    else:
        user_info_editable = False

    data = checkout_data_provider.get_data(step=step, user_info_editable=user_info_editable, user_email=user_email)
    return render_template('general/checkout.html', data=data)


@app.route('/faq')
@log_route
def faq():
    data = faq_data_provider.get_data()
    return render_template('general/faq.html', data=data)


@app.route('/')
@app.route('/home')
@log_route
def home():
    data = home_data_provider.get_data()
    return render_template('general/home.html', data=data)


@app.route('/minha-conta', methods=['GET', 'POST'])
@login_required
@log_route
def my_account():
    if request.method == 'GET':
        # Getting optional parameters
        user_info_editable = request.args.get("editar")

        # Setting default value to optional parameters
        if user_info_editable and user_info_editable == "sim":
            user_info_editable = True
        else:
            user_info_editable = False

        data = my_account_data_provider.get_data(user_info_editable)
        return render_template('general/my-account.html', data=data)

    elif request.method == 'POST':
        # TODO: Implement

        return redirect(url_for('my_account'))

    abort(404)


@app.route('/pedido/<int:order_id>')
@login_required
@log_route
def order(order_id):
    data = order_data_provider.get_data(order_id)
    return render_template('general/order.html', data=data)
