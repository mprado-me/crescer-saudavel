#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, redirect, render_template, request, url_for, session
from flask_login import login_required

from flask_app.data_providers.customer.general.about_us import about_us_data_provider
from flask_app.data_providers.customer.general.checkout import checkout_data_provider
from flask_app.data_providers.customer.general.faq import faq_data_provider
from flask_app.data_providers.customer.general.home import home_data_provider
from flask_app.data_providers.customer.general.my_account import my_account_data_provider
from flask_app.data_providers.customer.general.order import order_data_provider
from .. import app
from ..utils.decorators import log_route
from ..utils.exceptions import log_unrecognized_exception


@app.route('/sobre-nos')
@log_route
def about_us():
    try:
        data = about_us_data_provider.get_data()
        return render_template('customer/general/about-us.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/finalizacao-de-compra/passo/<int:step>')
@login_required
@log_route
def checkout(step):
    try:
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
        return render_template('customer/general/checkout.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/faq')
@log_route
def faq():
    try:
        data = faq_data_provider.get_data()
        return render_template('customer/general/faq.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/')
@app.route('/home')
@log_route
def home():
    try:
        data = home_data_provider.get_data()
        return render_template('customer/general/home.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/minha-conta', methods=['GET', 'POST'])
@login_required
@log_route
def my_account():
    # GET
    if request.method == 'GET':
        try:
            # Getting optional parameters
            user_info_editable = request.args.get("editar")

            # Setting default value to optional parameters
            if user_info_editable and user_info_editable == "sim":
                user_info_editable = True
            else:
                user_info_editable = False

            data = my_account_data_provider.get_data(user_info_editable)
            return render_template('customer/general/my-account.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            # TODO: Implement
            return redirect(url_for('my_account'))
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/pedido/<int:order_id>')
@login_required
@log_route
def order(order_id):
    try:
        data = order_data_provider.get_data(order_id)
        return render_template('customer/general/order.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
