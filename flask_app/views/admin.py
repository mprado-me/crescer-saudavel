from flask import render_template, request, url_for, redirect, abort, session

from flask_app import app, db

from functools import wraps

from flask_login import login_required

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