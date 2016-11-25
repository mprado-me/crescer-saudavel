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
                name="a01",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a02",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a03",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a04",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a05",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a06",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a07",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a08",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a09",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a10",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a11",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a12",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a13",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a14",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a15",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a16",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a17",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a18",
                category_id=1,
            ))
            db.session.add(Subcategory(
                name="a19",
                category_id=1,
            ))

            db.session.add(Subcategory(
                name="b01",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b02",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b03",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b04",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b05",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b06",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b07",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b08",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b09",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b10",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b11",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b12",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b13",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b14",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b15",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b16",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b17",
                category_id=2,
            ))
            db.session.add(Subcategory(
                name="b18",
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

            db.session.add(Subcategory(
                name="d1",
                category_id=4,
            ))
            db.session.add(Subcategory(
                name="d2",
                category_id=4,
            ))
            db.session.add(Subcategory(
                name="d3",
                category_id=4,
            ))

            db.session.add(Subcategory(
                name="e1",
                category_id=5,
            ))
            db.session.add(Subcategory(
                name="e2",
                category_id=5,
            ))
            db.session.add(Subcategory(
                name="e3",
                category_id=5,
            ))

            db.session.add(Subcategory(
                name="f1",
                category_id=6,
            ))
            db.session.add(Subcategory(
                name="f2",
                category_id=6,
            ))
            db.session.add(Subcategory(
                name="f3",
                category_id=6,
            ))
            db.session.add(Subcategory(
                name="f4",
                category_id=6,
            ))
            db.session.add(Subcategory(
                name="f5",
                category_id=6,
            ))

            db.session.add(Subcategory(
                name="g1",
                category_id=7,
            ))
            db.session.add(Subcategory(
                name="g2",
                category_id=7,
            ))

            db.session.add(Subcategory(
                name="h1",
                category_id=8,
            ))
            db.session.add(Subcategory(
                name="h2",
                category_id=8,
            ))
            db.session.add(Subcategory(
                name="h3",
                category_id=8,
            ))

            db.session.add(Subcategory(
                name="i1",
                category_id=9,
            ))

            db.session.add(Product(
                active=True,
                title ="P01",
                category_id = 1,
                subcategory_id = 1,
                price = Decimal("3.20"),
                stock_quantity = 26,
                stop_sell_stock_quantity = 3,
                summary = "Resumo do P01",

                image_1 = "1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P02",
                category_id=1,
                subcategory_id=1,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P02",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P03",
                category_id=2,
                subcategory_id=4,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P03",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P04",
                category_id=2,
                subcategory_id=5,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P04",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P05",
                category_id=2,
                subcategory_id=5,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P05",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=False,
                title="P06",
                category_id=2,
                subcategory_id=5,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P06",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=False,
                title="P07",
                category_id=2,
                subcategory_id=5,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P07",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P08",
                category_id=2,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P08",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P09",
                category_id=2,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P09",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P10",
                category_id=3,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P10",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P11",
                category_id=None,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P11",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P12",
                category_id=None,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P12",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P13",
                category_id=None,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P13",

                image_1="1.jpg",
                image_2="2.jpg",
            ))
            db.session.add(Product(
                active=True,
                title="P14",
                category_id=None,
                subcategory_id=None,
                price=Decimal("3.20"),
                stock_quantity=26,
                stop_sell_stock_quantity=3,
                summary="Resumo do P14",

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
