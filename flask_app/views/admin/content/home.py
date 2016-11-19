#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, request
from flask_login import login_required

from flask_app import app
from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


@app.route('/painel-administrativo/conteudo/home')
@login_required
@admin
@log_route
def admin_content_home():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/conteudo/home/mover-secao-para-cima/<int:section_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_content_home_move_section_up(section_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/conteudo/home/mover-secao-para-baixo/<int:section_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_content_home_move_section_down(section_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/conteudo/home/remover-secao/<int:section_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_content_home_remove_section(section_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/conteudo/home/editar-carousel', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_content_home_edit_carousel():
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


@app.route('/painel-administrativo/conteudo/home/adicionar-secao', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_content_home_add_section():
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


@app.route('/painel-administrativo/conteudo/home/editar-secao', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_content_home_edit_section():
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


@app.route('/painel-administrativo/conteudo/home/editar-blog-preview', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_content_home_edit_blog_preview():
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
