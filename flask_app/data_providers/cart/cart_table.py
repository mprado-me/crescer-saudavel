#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for


class CartTableDataProvider:
    def __init__(self):
        pass

    def get_fresh_order_data(self, user_email, editable):
        return self.get_sample_data_0(editable)

    def get_sample_data_0(self, editable):
        return {
            "editable": editable,
            "products": [
                {
                    "id": 1,
                    "image_href": url_for("static", filename="images/products/p8.jpg"),
                    "title": "Papinha de maça - 500g",
                    "unit_price": "R$ 10,00",
                    "quantity": 2,
                    "subtotal": "R$ 20,00",
                },
                {
                    "id": 2,
                    "image_href": url_for("static", filename="images/products/p8.jpg"),
                    "title": "Papinha de arroz doce - 200g",
                    "unit_price": "R$ 4,20",
                    "quantity": 3,
                    "subtotal": "R$ 12,60",
                },
            ],
        }

    def get_old_order_data(self, order_id):
        return self.get_sample_data_1()

    def get_sample_data_1(self):
        return {
            "editable": False,
            "products": [
                {
                    "id": 1,
                    "image_href": url_for("static", filename="images/products/p8.jpg"),
                    "title": "Papinha de maça - 500g",
                    "unit_price": "R$ 10,00",
                    "quantity": 2,
                    "subtotal": "R$ 20,00",
                },
                {
                    "id": 2,
                    "image_href": url_for("static", filename="images/products/p8.jpg"),
                    "title": "Papinha de arroz doce - 200g",
                    "unit_price": "R$ 4,20",
                    "quantity": 3,
                    "subtotal": "R$ 12,60",
                },
            ],
        }

cart_table_data_provider = CartTableDataProvider()
