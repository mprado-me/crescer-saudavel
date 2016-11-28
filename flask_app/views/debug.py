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

from flask import flash, redirect, url_for, render_template_string, request

if app.config["DEBUG"]:
    @app.route('/debug/db', methods=["GET"])
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
            <form action="{{url_for('clear_db')}}" method=post enctype=multipart/form-data>
                <input type=submit value="Limpar Db">
            </form>
            <form action="{{url_for('create_db')}}" method=post enctype=multipart/form-data>
                <input type=submit value="Criar Db">
            </form>
            <form action="{{url_for('fill_db')}}" method=post enctype=multipart/form-data>
                <input type=submit value="Preencher Db">
            </form>
        """)


    @app.route('/debug/db/restart', methods=["GET"])
    @log_route
    def restart_db():
        try:
            clear_db_implementation()
            create_db_implementation()
            fill_db_implementation()
            flash("Db foi reiniciado com sucesso", "success")
            return redirect(url_for("admin_dashboard"))
        except:
            flash("Falha ao reiniciar o db")
            return redirect(url_for('debug'))

    @app.route('/debug/db/clear', methods=["POST"])
    @log_route
    def clear_db():
        try:
            clear_db_implementation()
            flash("Db foi limpo com sucesso")
            return redirect(url_for('debug'))
        except Exception as e:
            log_unrecognized_exception(e)
            flash("Falha ao limpar o db")
            return redirect(url_for('debug'))


    def clear_db_implementation():
        db.drop_all()


    @app.route('/debug/db/create', methods=["POST"])
    @log_route
    def create_db():
        try:
            create_db_implementation()
            flash("Db foi criado com sucesso")
            return redirect(url_for('debug'))
        except Exception as e:
            log_unrecognized_exception(e)
            flash("Falha ao criar o db")
            return redirect(url_for('debug'))


    def create_db_implementation():
        db.create_all()


    @app.route('/debug/db/fill', methods=["POST"])
    @log_route
    def fill_db():
        try:
            fill_db_implementation()
            flash("Db preenchido com sucesso")
            return redirect(url_for('debug'))
        except Exception as e:
            db.session.rollback()
            log_unrecognized_exception(e)
            flash("Falha ao preencher o db")
            return redirect(url_for('debug'))


    def fill_db_implementation():
        email = app.config["ADMIN_MAIL"]
        admin_user = User(
            email=email,
            email_confirmed=True,
            authenticated=True,
        )
        admin_user.password = "aaaaaa"
        db.session.add(admin_user)

        db.session.add(Category(
            name="A",
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
            title="P01",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P01",

            image_1="1.jpg",
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
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P05",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P06",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P06",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P07",
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
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
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P14",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P15",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P15",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P17",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P17",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P17",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P17",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P18",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P18",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P19",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P19",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P20",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P20",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P21",
            category_id=1,
            subcategory_id=1,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P21",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P22",
            category_id=2,
            subcategory_id=4,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P22",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P23",
            category_id=2,
            subcategory_id=5,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P23",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P24",
            category_id=2,
            subcategory_id=5,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P24",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=False,
            title="P25",
            category_id=2,
            subcategory_id=5,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P25",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=False,
            title="P26",
            category_id=2,
            subcategory_id=5,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P26",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P27",
            category_id=2,
            subcategory_id=None,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P27",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P28",
            category_id=2,
            subcategory_id=None,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P28",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P29",
            category_id=3,
            subcategory_id=None,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P29",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P30",
            category_id=None,
            subcategory_id=None,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P30",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P31",
            category_id=None,
            subcategory_id=None,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P31",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P32",
            category_id=None,
            subcategory_id=None,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P32",

            image_1="1.jpg",
            image_2="2.jpg",
        ))
        db.session.add(Product(
            active=True,
            title="P33",
            category_id=None,
            subcategory_id=None,
            price=Decimal("3.20"),
            stock_quantity=26,
            stop_sell_stock_quantity=3,
            summary="Resumo do P33",

            image_1="1.jpg",
            image_2="2.jpg",
        ))

        db.session.commit()


    @app.route('/debug/test', methods=["GET", "POST"])
    @log_route
    def test():
        q = request.args.get("q")

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
                        #example{
                            margin-right: -20px;
                            margin-top: 20px;
                        }

                        .align-right {
                            text-align: right;
                        }
                    </style>
                </head>
                <body>
                    <div class="align-right">
                        <a data-placement="bottom" id="example" tabindex="0" class="btn btn-lg btn-danger" role="button" data-toggle="popover" data-trigger="focus" data-content="And here's some amazing content. It's very engaging. Right? And here's some amazing content. It's very engaging. Right? And here's some amazing content. It's very engaging. Right? And here's some amazing content. It's very engaging. Right?">Dismissible popover</a>
                    </div>

                    <script type="text/javascript" src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
                    <script type="text/javascript" src="{{ url_for('static', filename='js/bootstrap.min.js' )}}"></script>
                    <script>
                        $('#example').popover()
                    </script>
                </body>
            """)
        # POST
        else:
            return None
