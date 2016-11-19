#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask_app.utils.enums import OrderStatus

from flask import url_for


class HomeDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return self.sample_data_0()

    def sample_data_0(self):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.home),
            "n_new_orders": 3,
            "new_orders_href": url_for("admin_orders", order_status=OrderStatus.PAID, page=1),
        }
        return data

home_data_provider = HomeDataProvider()
