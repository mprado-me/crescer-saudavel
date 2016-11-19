#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, request
from flask_login import login_required

from flask_app import app
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/painel-administrativo/adicionar-blog-post', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_blog_post():
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


@app.route('/painel-administrativo/editar-blog-post/<int:post_id>', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_edit_blog_post(post_id):
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


@app.route('/painel-administrativo/blog-posts/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_blog_posts(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-blog-post/<int:post_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_remove_blog_post(post_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
