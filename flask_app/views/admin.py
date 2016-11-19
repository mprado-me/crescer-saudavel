#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from .. import app

from ..data_providers.admin.add_image import add_image_data_provider

from ..forms.admin import UploadImageForm

from ..utils.decorators import admin, log_route
from ..utils.exceptions import log_unrecognized_exception

from flask import abort, render_template, request

from flask_login import login_required

from werkzeug.utils import secure_filename


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


@app.route('/painel-administrativo/editar-produto/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_edit_product(product_id):
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


@app.route('/painel-administrativo/pedidos/status/<int:order_status>/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_orders(order_status, page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/desmarcar-pedido-como-enviado/<int:order_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_uncheck_order_as_shipped():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/marcar-pedido-como-enviado/<int:order_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_mark_order_as_shipped():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/desmarcar-pedido-como-entregue/<int:order_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_uncheck_order_as_delivered():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/marcar-pedido-como-entregue/<int:order_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_mark_order_as_delivered():
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/adicionar-produto', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_product():
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


@app.route('/painel-administrativo/produtos/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_products(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/adicionar-ao-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_add_to_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-do-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_remove_from_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/atualizar-estoque/<int:product_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_update_stock(product_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


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


@app.route('/painel-administrativo/clientes/cadastrados/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_registered_customers(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/clientes/newsletter/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_newsletter_customers(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/adicionar-imagem', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_image():
    form = UploadImageForm()

    # GET
    if request.method == "GET":
        try:
            data = add_image_data_provider.get_data(form=form)
            return render_template("admin/add-image.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = add_image_data_provider.get_data(form=form)
                return render_template("admin/add-image.html", data=data)

            file_ = request.files['file']
            filename = secure_filename(file_.filename)
            file_.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return "Imagem enviada"
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/imagens/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_images(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-imagem/<int:image_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_remove_image(image_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


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


@app.route('/painel-administrativo/cidades-atendidas/adicionar-cidade', methods=['GET', 'POST'])
@login_required
@admin
@log_route
def admin_add_attended_city():
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


@app.route('/painel-administrativo/cidades-atendidas/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_attended_cities(page):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-cidade-atendida/<int:city_id>', methods=["POST"])
@login_required
@admin
@log_route
def admin_remove_attended_city(section_id):
    try:
        raise NotImplementedError()
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
