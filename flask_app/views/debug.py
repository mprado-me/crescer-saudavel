#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal

from flask_app import app, db

from flask_app.models.user import User
from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory
from flask_app.models.product import Product

from flask_app.utils.exceptions import log_unrecognized_exception

from flask_app.utils.decorators import log_route

from flask import flash, redirect, url_for, render_template_string

if app.config["DEBUG"]:
    @app.route('/debug', methods=["GET"])
    @log_route
    def debug():
        return render_template_string("""
            {% with messages = get_flashed_messages() %}
                {% if messages %}
                    {% for message in messages %}
                        <p>{{message}}</p>
                    {% endfor %}
                {% endif %}
            {% endwith %}
            <form action="{{url_for('restart_db')}}" method=post enctype=multipart/form-data>
                <input type=submit value="Reiniciar Db">
            </form>
            <form action="{{url_for('fill_db')}}" method=post enctype=multipart/form-data>
                <input type=submit value="Preencher Db">
            </form>
        """)


    @app.route('/restart-db', methods=["POST"])
    @log_route
    def restart_db():
        try:
            db.drop_all()
            db.create_all()

            flash("Db foi reiniciado com sucesso")
            return redirect(url_for('debug'))
        except Exception as e:
            log_unrecognized_exception(e)
            flash("Falha ao reiniciar o db")
            return redirect(url_for('debug'))

    @app.route('/fill-db', methods=["POST"])
    @log_route
    def fill_db():
        try:
            email = app.config["ADMIN_MAIL"]
            admin_user = User(
                email=email,
                email_confirmed = True,
                authenticated = True,
            )
            admin_user.password = "aaaaaa"
            db.session.add(admin_user)

            db.session.add(Category(
                name = "A",
            ))
            db.session.add(Category(
                name="B",
            ))
            db.session.add(Category(
                name="C",
            ))
            db.session.add(Category(
                name="D",
            ))
            db.session.add(Category(
                name="E",
            ))
            db.session.add(Category(
                name="F",
            ))
            db.session.add(Category(
                name="G",
            ))
            db.session.add(Category(
                name="H",
            ))
            db.session.add(Category(
                name="I",
            ))
            db.session.add(Category(
                name="J",
            ))
            db.session.add(Category(
                name="K",
            ))
            db.session.add(Category(
                name="L",
            ))
            db.session.add(Category(
                name="M",
            ))
            db.session.add(Category(
                name="N",
            ))
            db.session.add(Category(
                name="O",
            ))
            db.session.add(Category(
                name="P",
            ))
            db.session.add(Category(
                name="Q",
            ))
            db.session.add(Category(
                name="R",
            ))
            db.session.add(Category(
                name="S",
            ))
            db.session.add(Category(
                name="T",
            ))

            db.session.add(Subcategory(
                name="a1",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a2",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a3",
                category_id=1,
            ))

            db.session.add(Subcategory(
                name="b1",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b2",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b3",
                category_id=2,
            ))

            db.session.add(Subcategory(
                name="c1",
                category_id=3,
            ))
            db.session.add(Subcategory(
                name="c2",
                category_id=3,
            ))

            db.session.add(Product(
                active=True,
                title ="Produto 01",
                category_id = 1,
                subcategory_id = 1,
                price = Decimal("3.20"),
                stock_quantity = 26,
                stop_sell_stock_quantity = 3,
                summary = "Resumo do Produto 1",

                image_1 = "1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 02",
                category_id=1,
                subcategory_id=1,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 2",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 03",
                category_id=2,
                subcategory_id=4,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 3",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 04",
                category_id=2,
                subcategory_id=5,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 4",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 05",
                category_id=2,
                subcategory_id=5,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 5",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=False,
                title="Produto 06",
                category_id=2,
                subcategory_id=5,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 6",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=False,
                title="Produto 07",
                category_id=2,
                subcategory_id=5,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 7",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 08",
                category_id=2,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 8",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 09",
                category_id=2,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 9",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 10",
                category_id=3,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 10",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 11",
                category_id=None,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 11",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 12",
                category_id=None,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 12",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 13",
                category_id=None,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 13",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="Produto 14",
                category_id=None,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do Produto 14",

                image_1="1.jpg",
                image_2="2.jpg",
            ))

            db.session.commit()

            flash("Db preenchido com sucesso")
            return redirect(url_for('debug'))
        except Exception as e:
            db.session.rollback()
            log_unrecognized_exception(e)
            flash("Falha ao preencher o db")
            return redirect(url_for('debug'))
