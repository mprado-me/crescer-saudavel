#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort
from flask_login import login_required

from flask_app import app
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/painel-administrativo/pedidos/status/<int:order_status>/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_orders(order_status, page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/desmarcar-pedido-como-enviado/<int:order_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_uncheck_order_as_shipped():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/marcar-pedido-como-enviado/<int:order_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_mark_order_as_shipped():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/desmarcar-pedido-como-entregue/<int:order_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_uncheck_order_as_delivered():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/marcar-pedido-como-entregue/<int:order_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_mark_order_as_delivered():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
