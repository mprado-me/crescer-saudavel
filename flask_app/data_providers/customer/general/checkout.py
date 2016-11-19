#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for

from flask_app.data_providers.customer.cart.cart_table import cart_table_data_provider

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider
from flask_app.data_providers.customer.shared.user_info import user_info_data_provider
from flask_app.data_providers.customer.shared.total_table import total_table_data_provider


class CheckoutDataProvider:
    def __init__(self):
        pass

    def get_data(self, step, user_info_editable, user_email):
        return self.sample_data_0(step=step, user_info_editable=user_info_editable, user_email=user_email)

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Finalização de compra",
                },
            ],
            "title": "Finalização de compra",
        }

    def sample_data_0(self, step, user_info_editable, user_email):
        data = {
            "user_info_editable": user_info_editable,
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "footer_data": footer_data_provider.get_data(),
            "step": step,
            "user_info_data": user_info_data_provider.get_data(user_info_editable),
            "cart_table_data": cart_table_data_provider.get_fresh_order_data(user_email=user_email, editable=False),
            "total_table_data": total_table_data_provider.get_fresh_order_data(user_email=user_email),
        }
        return data

checkout_data_provider = CheckoutDataProvider()
