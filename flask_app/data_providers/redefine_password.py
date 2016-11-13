#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..utils.exceptions import DatabaseAccessError

from header import HeaderDataProvider
from footer import FooterDataProvider

from flask import url_for


class RedefinePasswordDataProvider:
    def __init__(self):
        pass

    def get_data(self, form, email, token):
        return self.sample_data_0(form=form, email=email, token=token)

    def get_data_when_database_access_error(self, form, email, token):
        data = self.get_data(form=form, email=email, token=token)
        msgs = [DatabaseAccessError.msg]
        data["msgs"] = msgs
        return data

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
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "token": token,
            "email": email,
            "form": form,
            "footer_data": FooterDataProvider().get_data(),
        }
        return data

redefine_password_data_provider = RedefinePasswordDataProvider()
