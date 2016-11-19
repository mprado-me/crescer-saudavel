#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.cart.cart_table import cart_table_data_provider

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider
from flask_app.data_providers.customer.shared.total_table import total_table_data_provider

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
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(order_id),
            "cart_table_data": cart_table_data_provider.get_old_order_data(order_id=order_id),
            "total_table_data": total_table_data_provider.get_old_order_data(order_id=order_id),
            "footer_data": footer_data_provider.get_data(),
        }
        return data

order_data_provider = OrderDataProvider()
