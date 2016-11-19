#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider

from flask import url_for


class SentConfirmationEmailDataProvider:
    def __init__(self):
        pass

    def get_data(self, email):
        return self.sample_data_0(email)

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Criar conta",
                    "href": url_for("create_account"),
                },
                {
                    "name": "Confirmação do email",
                },
            ],
            "title": "Confirmação do email",
        }

    def sample_data_0(self, email):
        data = {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "email": email,
            "footer_data": footer_data_provider.get_data(),
        }
        return data

sent_confirmation_email_data_provider = SentConfirmationEmailDataProvider()
