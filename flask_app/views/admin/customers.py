#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort
from flask_login import login_required

from flask_app import app
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/painel-administrativo/clientes/cadastrados/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_registered_customers(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/clientes/newsletter/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_newsletter_customers(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
