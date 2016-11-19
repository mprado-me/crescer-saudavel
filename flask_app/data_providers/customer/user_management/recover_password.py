#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider

from flask_app.utils.exceptions import DatabaseAccessError
from flask_app.utils.exceptions import EmailSendingError

from flask import url_for


class RecoverPasswordDataProvider:
    def __init__(self):
        pass

    def get_data(self, form):
        return self.sample_data_0(form=form)

    def get_data_when_database_access_error(self, form):
        data = self.get_data(form=form)
        data["msgs"] = [DatabaseAccessError.msg]
        return data

    def get_data_when_email_sending_error(self, form):
        data = self.get_data(form=form)
        data["msgs"] = [EmailSendingError.msg]
        return data

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Entrar",
                    "href": url_for("login"),
                },
                {
                    "name": "Recuperar senha",
                },
            ],
            "title": "Recuperar senha",
        }

    def sample_data_0(self, form):
        data = {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "form": form,
            "footer_data": footer_data_provider.get_data(),
        }
        return data

recover_password_data_provider = RecoverPasswordDataProvider()
