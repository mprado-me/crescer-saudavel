#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..utils.decorators import admin, log_route

from flask_login import login_required

@app.route('/painel-administrativo')
@login_required
@admin
@log_route
def admin_dashboard():
    return "Seja bem vindo admin!"
