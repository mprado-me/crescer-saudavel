#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider

from flask_app.utils.exceptions import DatabaseAccessError
from flask_app.utils.exceptions import EmailSendingError

from flask import url_for


class ResendConfirmationEmailDataProvider:
    def __init__(self):
        pass

    def get_data(self, form):
        return self.sample_data_0(form=form)

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Reenviar email de confirmação",
                },
            ],
            "title": "Reenviar email de confirmação",
        }

    def sample_data_0(self, form):
        data = {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "form": form,
            "footer_data": footer_data_provider.get_data(),
        }
        return data

resend_confirmation_email_data_provider = ResendConfirmationEmailDataProvider()
