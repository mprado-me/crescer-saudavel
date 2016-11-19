#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, render_template
from flask_login import login_required

from flask_app import app

from flask_app.data_providers.admin.general.home import home_data_provider

from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/painel-administrativo')
@login_required
@admin
@log_route
def admin_dashboard():
    try:
        data = home_data_provider.get_data()
        return render_template("admin/general/home.html", data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
