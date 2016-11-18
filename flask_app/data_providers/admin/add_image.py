#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.admin.navbar import navbar_data_provider


class AddImageDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return self.sample_data_0()

    def sample_data_0(self):
        data = {
            "navbar_data": navbar_data_provider.get_data(),
        }
        return data

add_image_data_provider = AddImageDataProvider()
