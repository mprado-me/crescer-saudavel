#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, request
from flask_login import login_required

from flask_app import app
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/painel-administrativo/adicionar-produto', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_product():
    form = None

    # GET
    if request.method == "GET":
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/editar-produto/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_edit_product(product_id):
    form = None

    # GET
    if request.method == "GET":
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            raise NotImplementedError()
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/produtos/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_products(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/adicionar-ao-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_add_to_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-do-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_remove_from_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/atualizar-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_update_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
