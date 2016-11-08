#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider

from flask import url_for


class LoginDataProvider:
    def __init__(self):
        pass

    def get_data(self, form, msgs=None):
        return self.sample_data_0(form, msgs)

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Entrar",
                },
            ],
            "title": "Entrar",
        }

    def sample_data_0(self, form, msgs):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "msgs": msgs,
            "form": form,
            "footer_data": FooterDataProvider().get_data(),
        }
        return data

login_data_provider = LoginDataProvider()
