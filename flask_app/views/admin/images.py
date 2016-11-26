#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import os
import time
import random

from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename

from flask_app import app

from flask_app.data_providers.admin.images.images import images_data_provider

from flask_app.forms.admin import SimpleSubmitForm, UploadImageForm

from flask_app.utils.decorators import admin, log_route
from flask_app.utils.exceptions import InsecurePostException, log_unrecognized_exception


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
    url_args = {
        "page": page
    }

    try:
        data = images_data_provider.get_data(page=page, remove_form=remove_form, url_args=url_args)
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

    # if random.uniform(0,1) < 0.5:
    #     return ("", 500)

    try:
        # Getting optional parameters
        url_args = request.args.get('url_args')

        # Setting default value to optional parameters
        # Converting optional parameters from string type to its corresponded python type
        if not url_args:
            url_args = {}
        else:
            url_args = ast.literal_eval(url_args)

        if not remove_form.validate_on_submit():
            raise InsecurePostException()

        path_to_file = os.path.join(app.config['UPLOADED_IMAGES_FOLDER'], image_name)
        if os.path.exists(path_to_file):
            os.remove(path_to_file)

        flash("Imagem \"%s\" foi removida com sucesso." % image_name, "success")
        return ('', 204)
        # return redirect(url_for("admin_images", **url_args))
    except Exception as e:
        log_unrecognized_exception(e)
        return ("", 500)
