#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider


class FailedToGetDataProvider:
    def __init__(self):
        pass

    def get_data(self, current_url):
        return {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "button": {
                "title": "Tentar novamente",
                "href": current_url,
            },
            "footer_data": footer_data_provider.get_data(),
        }

    def get_page_heading_data(self):
        return {
            "title": "Falha",
        }

failed_to_get_data_provider = FailedToGetDataProvider()
