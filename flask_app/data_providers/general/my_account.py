#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for

from flask_app.data_providers.shared.footer import FooterDataProvider
from flask_app.data_providers.shared.header import HeaderDataProvider
from flask_app.data_providers.shared.user_info import UserInfoDataProvider


class MyAccountDataProvider:
    def __init__(self):
        pass

    def get_data(self, editable):
        return self.sample_data_1(editable)

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Minha conta",
                },
            ],
            "title": "Minha conta",
        }

    def sample_data_0(self, editable):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "user_info_data": UserInfoDataProvider().get_data(editable),
            "orders": [
                {
                    "id": 123,
                    "date": "05/12/2015",
                    "total": "R$ 125,00",
                    "status": "Empacotando",
                },
                {
                    "id": 12312,
                    "date": "05/11/2015",
                    "total": "R$ 65,00",
                    "status": "Enviado",
                },
                {
                    "id": 1213,
                    "date": "05/10/2015",
                    "total": "R$ 25,00",
                    "status": "Entregue",
                },
            ],
            "footer_data": FooterDataProvider().get_data(),
        }
        return data

    def sample_data_1(self, editable):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": {
                "path": [
                    {
                        "name": "Home",
                        "href": url_for("home"),
                    },
                    {
                        "name": "Minha conta",
                    },
                ],
                "title": "Minha conta",
            },
            "user_info_data": UserInfoDataProvider().get_data(editable),
            "orders": [],
            "footer_data": FooterDataProvider().get_data(),
        }
        return data

my_account_data_provider = MyAccountDataProvider()

