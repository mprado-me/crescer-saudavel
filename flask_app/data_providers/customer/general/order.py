#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.cart.cart_table import CartTableDataProvider

from flask_app.data_providers.customer.shared.footer import FooterDataProvider
from flask_app.data_providers.customer.shared.header import HeaderDataProvider
from flask_app.data_providers.customer.shared.total_table import TotalTableDataProvider

from flask import url_for


class OrderDataProvider:
    def __init__(self):
        pass

    def get_data(self, order_id):
        return self.sample_data_0(order_id)

    def get_page_heading_data(self, order_id):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Minha conta",
                    "href": url_for('my_account'),
                },
                {
                    "name": "Pedido",
                },
            ],
            "title": "Pedido #" + str(order_id),
        }

    def sample_data_0(self, order_id):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(order_id),
            "cart_table_data": CartTableDataProvider().get_old_order_data(order_id=order_id),
            "total_table_data": TotalTableDataProvider().get_old_order_data(order_id=order_id),
            "footer_data": FooterDataProvider().get_data(),
        }
        return data

order_data_provider = OrderDataProvider()
