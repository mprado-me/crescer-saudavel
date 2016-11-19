#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.shared.footer import FooterDataProvider
from flask_app.data_providers.customer.shared.header import HeaderDataProvider

from flask_app.utils.exceptions import DatabaseAccessError
from flask_app.utils.exceptions import EmailSendingError

from flask import url_for


class CreateAccountDataProvider:
    def __init__(self):
        pass

    def get_data(self, form):
        return self.sample_data_0(form)

    def get_data_when_database_access_error(self, form):
        data = self.get_data(form=form)
        data["msg"] = DatabaseAccessError.msg
        return data

    def get_data_when_email_sending_error(self, form):
        data = self.get_data(form=form)
        data["msg"] = EmailSendingError.msg
        return data

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Criar conta",
                },
            ],
            "title": "Criar conta",
        }

    def sample_data_0(self, form):
        return {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "form": form,
            "footer_data": FooterDataProvider().get_data(),
        }

create_account_data_provider = CreateAccountDataProvider()
