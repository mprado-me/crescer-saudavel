#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, request
from flask_login import login_required

from flask_app import app
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/painel-administrativo/cidades-atendidas/adicionar-cidade', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_attended_city():
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


@app.route('/painel-administrativo/cidades-atendidas/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_attended_cities(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-cidade-atendida/<int:city_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_remove_attended_city(section_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
