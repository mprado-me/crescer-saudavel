#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..data_providers.admin.add_image import add_image_data_provider

from ..utils.decorators import admin, log_route
from ..utils.exceptions import log_unrecognized_exception

from flask import abort, render_template, request

from flask_login import login_required

@app.route('/painel-administrativo')
@login_required
@admin
@log_route
def admin_dashboard():
    try:
        return "Seja bem vindo admin!"
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/adicionar-imagem', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def add_image():
    # GET
    if request.method == "GET":
        try:
            data = add_image_data_provider.get_data()
            return render_template("admin/add-image.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            return "Imagem enviada"
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)
