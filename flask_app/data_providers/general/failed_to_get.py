#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.shared.footer import FooterDataProvider
from flask_app.data_providers.shared.header import HeaderDataProvider


class FailedToGetDataProvider:
    def __init__(self):
        pass

    def get_data(self, msg, button):
        return self.sample_data_0(msg=msg, button=button)

    def get_data_when_database_access_error(self, href):
        msg = {
            "type": "danger",
            "content": "Falha! Ocorreu um erro ao acessar o banco de dados.",
        }
        button = {
            "title": "Tentar novamente",
            "href": href,
        }
        return self.get_data(msg=msg, button=button)

    def get_page_heading_data(self):
        return {
            "title": "Falha",
        }

    def sample_data_0(self, msg, button):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "msg": msg,
            "button": button,
            "footer_data": FooterDataProvider().get_data(),
        }
        return data

failed_to_get_data_provider = FailedToGetDataProvider()
