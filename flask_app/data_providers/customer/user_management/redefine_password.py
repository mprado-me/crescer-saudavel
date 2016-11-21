#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider

from flask_app.utils.exceptions import DatabaseAccessError

from flask import url_for


class RedefinePasswordDataProvider:
    def __init__(self):
        pass

    def get_data(self, form, email, token):
        return self.sample_data_0(form=form, email=email, token=token)

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Redefinir senha",
                },
            ],
            "title": "Redefinir senha",
        }

    def sample_data_0(self, form, email, token):
        data = {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "token": token,
            "email": email,
            "form": form,
            "footer_data": footer_data_provider.get_data(),
        }
        return data

redefine_password_data_provider = RedefinePasswordDataProvider()
