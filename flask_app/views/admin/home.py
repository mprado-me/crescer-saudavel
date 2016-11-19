#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort
from flask_login import login_required

from flask_app import app
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


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
