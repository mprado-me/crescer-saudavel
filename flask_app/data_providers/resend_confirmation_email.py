#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..utils.exceptions import DatabaseAccessError
from ..utils.exceptions import EmailSendingError

from header import HeaderDataProvider
from footer import FooterDataProvider

from flask import url_for


class ResendConfirmationEmailDataProvider:
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
                    "name": "Reenviar email de confirmação",
                },
            ],
            "title": "Reenviar email de confirmação",
        }

    def sample_data_0(self, form):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "form": form,
            "footer_data": FooterDataProvider().get_data(),
        }
        return data

resend_confirmation_email_data_provider = ResendConfirmationEmailDataProvider()
