#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider

from flask import url_for


class CreateAccountDataProvider:
    def __init__(self):
        pass

    def get_data(self, form, msg=None):
        return self.sample_data_0(form, msg)

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

    def sample_data_0(self, form, msg):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "form": form,
            "msg": msg,
            "footer_data": FooterDataProvider().get_data(),
        }
        return data
