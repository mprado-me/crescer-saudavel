#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider


class GetFailDataProvider:
    def __init__(self):
        pass

    def get_data(self, msg, button):
        return self.sample_data_0(msg, button)

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

get_fail_data_provider = GetFailDataProvider()
