#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import abort, render_template, request
from flask_login import login_required
from werkzeug.utils import secure_filename

from flask_app import app

from flask_app.data_providers.admin.images.add_image import add_image_data_provider

from flask_app.forms.admin import UploadImageForm

from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import log_unrecognized_exception


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
            return render_template("admin/images/add-image.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = add_image_data_provider.get_data(form=form)
                return render_template("admin/images/add-image.html", data=data)

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
