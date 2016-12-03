#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, random, shutil, string

from decimal import Decimal

from flask_app import app, db

from flask_app.data_providers.admin.images.images import images_data_provider

from flask_app.models.user import User
from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory
from flask_app.models.product import Product

from flask_app.utils.exceptions import log_unrecognized_exception

from flask_app.utils.decorators import log_route

from flask import redirect, url_for, render_template_string, request

if app.config["DEBUG"]:
    @app.route('/debug/images/restart', methods=["GET"])
    @log_route
    def restart_images():
        try:
            restart_images_implementation()
            return redirect(url_for("admin_dashboard"))
        except Exception as e:
            log_unrecognized_exception(e)
            return "Falha ao reiniciar as imagens"

    def restart_images_implementation():
        destiny_folder_path = app.config["UPLOADED_IMAGES_FOLDER"]
        for file_name in os.listdir(destiny_folder_path):
            file_path = os.path.join(app.config['UPLOADED_IMAGES_FOLDER'], file_name)
            if os.path.exists(file_path):
                os.remove(file_path)

        src_folder_path = "/vagrant/images"
        for file_name in os.listdir(src_folder_path):
            file_path = os.path.join(src_folder_path, file_name)
            if os.path.exists(file_path):
                shutil.copy(file_path, destiny_folder_path)

    @app.route('/debug/db/restart', methods=["GET"])
    @log_route
    def restart_db():
        try:
            clear_db_implementation()
            create_db_implementation()
            fill_db_implementation()
            return redirect(url_for("admin_dashboard"))
        except Exception as e:
            log_unrecognized_exception(e)
            return "Falha ao reiniciar o db"

    def clear_db_implementation():
        db.drop_all()

    def create_db_implementation():
        db.create_all()

    def fill_db_implementation():
        # Creating admin user
        email = app.config["ADMIN_MAIL"]
        admin_user = User(
            email=email,
            email_confirmed=True,
            authenticated=True,
        )
        # noinspection SpellCheckingInspection
        admin_user.password = "aaaaaa"
        db.session.add(admin_user)
        db.session.commit()

        # Creating default categories
        for i in range(0, 10):
            db.session.add(get_random_category())
            db.session.commit()

        # Creating default subcategories
        for i in range(0, 50):
            db.session.add(get_random_subcategory())
            db.session.commit()

        # Creating default products
        for i in range(50, 500):
            db.session.add(get_random_product())
            db.session.commit()

        # Creating categories to test paginator
        create_test_paginator_categories_and_products()

    def create_test_paginator_categories_and_products():
        per_page = app.config["ADMIN_N_PRODUCTS_PER_PAGE"]
        for i in range(0, 12):
            category = get_random_category()
            category.name = "categoria_%02d_paginas" % (i+1)
            db.session.add(category)
            db.session.commit()

            for j in range(0, per_page/2 + i*per_page):
                product = get_random_product()
                product.active = True
                product.category_id = category.id
                db.session.add(product)
            db.session.commit()

    def get_random_category():
        return Category(
            name=get_random_category_name()
        )

    def get_random_subcategory():
        return Subcategory(
            name=get_random_subcategory_name(),
            category_id=get_random_valid_category_id()
        )

    def get_random_product():
        random_value = random.uniform(0, 1)
        category_id = None
        subcategory_id = None
        if random_value < 0.6:
            category_id = get_random_valid_category_id(),
            subcategory_id = get_random_valid_subcategory_id(category_id=category_id),
        elif random_value < 0.9:
            category_id = get_random_valid_category_id(),

        return Product(
            active=(random.uniform(0, 1) < 0.5),
            title=get_random_title(),
            category_id=category_id,
            subcategory_id=subcategory_id,
            price=Decimal(get_random_price()),
            stock=get_random_stock(),
            min_stock=get_random_min_stock(),
            summary=get_random_summary(),
            sales_number=get_random_sales_number(),
            **get_random_images_dic()
        )

    def get_random_valid_category_id():
        return random.choice(Category.query.with_entities(Category.id).all())

    def get_random_valid_subcategory_id(category_id):
        try:
            return random.choice(Subcategory.query.filter(Subcategory.category_id==category_id).with_entities(Subcategory.id).all())
        except:
            return None

    def get_random_category_name():
        return get_random_string(random.randint(4, 8))

    def get_random_subcategory_name():
        return get_random_string(random.randint(4, 8))

    def get_random_title():
        s = ""
        for _ in range(random.randint(3, 6)):
            s += get_random_string(random.randint(3, 8))
            s += " "
        return s[:-1]

    def get_random_summary():
        s = ""
        for _ in range(random.randint(20, 100)):
            s += get_random_string(random.randint(3, 8))
            s += " "
        return s[:-1]

    def get_random_string(size):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(size))

    def get_random_price():
        s = get_random_digit()
        if random.uniform(0, 1) < 0.5:
            s += get_random_digit()
        s += "."
        s += get_random_digit()
        s += get_random_digit()

        return s

    def get_random_digit():
        return random.choice(string.digits)

    def get_random_stock():
        return random.randint(0, 500)

    def get_random_min_stock():
        return random.randint(2, 20)

    images_key_list = [
        "image_1",
        "image_2",
        "image_3",
        "image_4",
        "image_5",
        "image_6",
        "image_7",
        "image_8",
        "image_9",
        "image_10",
    ]

    def get_random_images_dic():
        images_key_list_copy = list(images_key_list)
        dic = {images_key_list_copy.pop(0): get_random_image_name()}
        for i in range(0, 9):
            dic[images_key_list_copy.pop(random.randint(0, len(images_key_list_copy)-1))] = get_random_image_name()
        return dic

    def get_random_image_name():
        return random.choice(images_data_provider.get_images_name_sorted())

    def get_random_sales_number():
        return random.randint(0, 500)

    @app.route('/debug/test', methods=["GET", "POST"])
    @log_route
    def test():
        # GET
        if request.method == "GET":
            return render_template_string("""
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    <title>{% block title %}{% endblock %}</title>
                    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=no">
                    <link rel="icon" href="#" type="image/x-icon">
                    <link rel="shortcut icon" href="#" type="image/x-icon">

                    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles/bootstrap.min.css') }}">
                    <meta name="viewport" content="initial-scale=1.0, width=device-width">

                    <style>
                        p {
                            color: red;
                        }

                        p#my-id-2 {
                            color: blue;
                        }
                    </style>
                </head>
                <body>
                    <p id="my-id-1">Oiiiii</p>
                    <p id="my-id-2">Oiiiii</span>
                </body>
            """)
        # POST
        else:
            return None
