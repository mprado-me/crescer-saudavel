#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..utils.decorators import admin, log_route
from ..utils.exceptions import log_unrecognized_exception

from flask import abort

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
