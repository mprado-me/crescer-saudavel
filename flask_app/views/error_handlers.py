#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import app


@app.errorhandler(404)
def page_not_found(e):
    return "Página não encontrada", 404