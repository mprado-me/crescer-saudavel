#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from flask import redirect, session, url_for
from flask_login import login_required
from functools import wraps

def admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session["user_id"] != app.config['ADMIN_MAIL']:
            return redirect(url_for('home'))
        return func(*args, **kwargs)
    return decorated_function

@app.route('/painel-administrativo')
@login_required
@admin
def admin_dashboard():
    return "Seja bem vindo admin!"