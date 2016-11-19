#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.cart.cart_table import CartTableDataProvider

from flask_app.data_providers.customer.shared.footer import FooterDataProvider
from flask_app.data_providers.customer.shared.header import HeaderDataProvider
from flask_app.data_providers.customer.shared.total_table import TotalTableDataProvider

from flask import url_for


class CartDataProvider:
    def __init__(self):
        pass

    def get_data(self, user_email):
        return self.sample_data_0(user_email=user_email)

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Meu carrinho",
                },
            ],
            "title": "Meu carrinho",
        }

    def sample_data_0(self, user_email):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "footer_data": FooterDataProvider().get_data(),
            "cart_table_data": CartTableDataProvider().get_fresh_order_data(user_email=user_email, editable=True),
            "total_table_data": TotalTableDataProvider().get_fresh_order_data(user_email=user_email),
        }
        return data


cart_data_provider = CartDataProvider()
