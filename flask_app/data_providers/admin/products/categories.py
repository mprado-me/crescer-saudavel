#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask_app.utils.decorators import append_request_msg


class CategoriesDataProvider():
    def __init__(self):
        pass

    @append_request_msg
    def get_add_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "form": form,
        }
        return data

    def get_edit_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "form": form,
        }
        return data

    def get_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
        }
        return data


categories_data_provider = CategoriesDataProvider()
