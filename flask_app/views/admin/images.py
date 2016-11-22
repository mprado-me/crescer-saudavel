#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename

from flask_app import app

from flask_app.data_providers.admin.images.images import images_data_provider

from flask_app.forms.admin import SimpleSubmitForm, UploadImageForm

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
            data = images_data_provider.get_add_data(form=form)
            return render_template("admin/images/add-image.html", data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = images_data_provider.get_add_data(form=form)
                return render_template("admin/images/add-image.html", data=data)

            image = request.files[form.image.name]
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOADED_IMAGES_FOLDER'], filename))

            flash("Imagem \"%s\" foi adicionada com sucesso." % filename, "success")
            return redirect(url_for("admin_add_image"))
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/painel-administrativo/imagens/pagina/<int:page>')
@login_required
@admin
@log_route
def admin_images(page):
    remove_form = SimpleSubmitForm()

    try:
        data = images_data_provider.get_data(page=page, remove_form=remove_form)
        return render_template("admin/images/images.html", data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/painel-administrativo/remover-imagem/<string:image_name>', methods=["POST"])
@login_required
@admin
@log_route
def admin_remove_image(image_name):
    remove_form = SimpleSubmitForm()

    # Getting optional parameters
    page_to_return = request.args.get('page_to_return')

    # Setting default value to optional parameters
    if not page_to_return:
        page_to_return = 1

    if not remove_form.validate_on_submit():
        flash("Não foi possível remover a imagem \"%s\". Tente novamente." % image_name, "warning")
        return redirect(url_for("admin_images", page=page_to_return))

    try:
        path_to_file = os.path.join(app.config['UPLOADED_IMAGES_FOLDER'], image_name)
        if os.path.exists(path_to_file):
            os.remove(path_to_file)

        flash("Imagem \"%s\" foi removida com sucesso." % image_name, "success")
        return redirect(url_for("admin_images", page=page_to_return))
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
