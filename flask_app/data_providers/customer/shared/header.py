#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.utils.enums import ProductSortMethod

from flask import url_for


class HeaderDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return self.get_sample_data_0()

    def get_sample_data_0(self):
        data = {
            "logged": False,
            "first_name": "João",
            "menu_data": [
                {
                    "name": "Produtos",
                    "href": url_for('products', page=1, sort_method=ProductSortMethod.NAME),
                    "children": [
                        {
                            "name": "Frutas",
                            "href": url_for('products', category_id=0, page=1, sort_method=ProductSortMethod.NAME),
                        },
                        {
                            "name": "Sopa creme",
                            "href": url_for('products', category_id=1, page=1, sort_method=ProductSortMethod.NAME),
                        },
                        {
                            "name": "Sopa com pedaços",
                            "href": url_for('products', category_id=2, page=1, sort_method=ProductSortMethod.NAME),
                        },
                        {
                            "name": "Linha Single",
                            "href": url_for('products', category_id=3, page=1, sort_method=ProductSortMethod.NAME),
                            "children": [
                                {
                                    "name": "Sobremesas",
                                    "href": url_for('products', category_id=3,
                                                    subcategory_id=0, page=1, sort_method=ProductSortMethod.NAME),
                                },
                            ]
                        },
                        {
                            "name": "Linha Emporinho",
                            "href": url_for('products', category_id=4, page=1, sort_method=ProductSortMethod.NAME),
                            "children": [
                                {
                                    "name": "Risotos",
                                    "href": url_for('products', category_id=4,
                                                    subcategory_id=0, page=1, sort_method=ProductSortMethod.NAME),
                                },
                                {
                                    "name": "Massas",
                                    "href": url_for('products', category_id=4,
                                                    subcategory_id=1, page=1, sort_method=ProductSortMethod.NAME),
                                },
                                {
                                    "name": "Escondidinhos",
                                    "href": url_for('products', category_id=4,
                                                    subcategory_id=2, page=1, sort_method=ProductSortMethod.NAME),
                                },
                                {
                                    "name": "Arroz",
                                    "href": url_for('products', category_id=4,
                                                    subcategory_id=3, page=1, sort_method=ProductSortMethod.NAME),
                                },
                                {
                                    "name": "Legumes",
                                    "href": url_for('products', category_id=4,
                                                    subcategory_id=4, page=1, sort_method=ProductSortMethod.NAME),
                                },
                                {
                                    "name": "Sopas/Cremes",
                                    "href": url_for('products', category_id=4,
                                                    subcategory_id=5, page=1, sort_method=ProductSortMethod.NAME),
                                },
                                {
                                    "name": "Refeições combinadas",
                                    "href": url_for('products', category_id=4,
                                                    subcategory_id=6, page=1, sort_method=ProductSortMethod.NAME),
                                },
                            ]
                        },
                        {
                            "name": "Acessórios",
                            "href": url_for('products', category_id=5, page=1, sort_method=ProductSortMethod.NAME),
                        },
                    ]
                },
                {
                    "name": "Blog",
                    "href": url_for('blog', page=1),
                },
            ],
            "cart_data": {
                "n_items": 5,
                "total_price": "R$ 32,60",
                "products": [
                    {
                        "title": "Papinha de maça - 500g",
                        "href": url_for('product', product_id=0),
                        "img_src": url_for("static", filename="images/products/p4.jpg"),
                        "quantity": 2,
                        "unity_price": "R$ 10,00"
                    },
                    {
                        "title": "Papinha de arroz doce - 200g",
                        "href": url_for('product', product_id=1),
                        "img_src": url_for("static", filename="images/products/p4.jpg"),
                        "quantity": 3,
                        "unity_price": "R$ 4,20"
                    }
                ]
            }
        }
        return data

    def get_sample_data_1(self):
        data = {
            "logged": False,
            "first_name": "João",
            "menu_data": [
                {
                    "name": "Produtos",
                    "href": url_for('products', page=1, sort_method=ProductSortMethod.NAME),
                    "children": [
                        {
                            "name": "Frutas",
                            "href": url_for('products', category_id=0, page=1, sort_method=ProductSortMethod.NAME),
                        },
                        {
                            "name": "Sopa creme",
                            "href": url_for('products', category_id=1, page=1, sort_method=ProductSortMethod.NAME),
                        },
                        {
                            "name": "Sopa com pedaços",
                            "href": url_for('products', category_id=2, page=1, sort_method=ProductSortMethod.NAME),
                        },
                    ]
                },
                {
                    "name": "Blog",
                    "href": url_for('blog', page=1),
                },
            ],
            "cart_data": {
                "n_items": 0,
                "total_price": "R$ 0,00",
                "products": []
            }
        }
        return data

header_data_provider = HeaderDataProvider()
