#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, request
from flask_login import login_required

from flask_app import app
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/painel-administrativo/conteudo/faq')
@login_required
@admin
@log_route
def admin_content_faq():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/conteudo/editar-faq', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_content_edit_faq():
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
