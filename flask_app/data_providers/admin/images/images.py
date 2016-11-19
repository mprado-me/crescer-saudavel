#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask_app.utils.decorators import append_request_msg


class ImagesDataProvider:
    def __init__(self):
        pass

    @append_request_msg
    def get_data(self, page):
        return self.sample_data_0(page=page)

    def sample_data_0(self, page):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.images),
        }
        return data

images_data_provider = ImagesDataProvider()
