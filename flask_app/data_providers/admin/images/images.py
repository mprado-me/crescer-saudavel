#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import app

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask_app.data_providers.shared.paginator import paginator_data_provider

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
            "paginator_data": paginator_data_provider.get_data(
                current_page=page,
                n_pages=app.config["N_PAGES_IN_ADMIN_IMAGES"],
                total_n_pages=10,
                url_endpoint="admin_images",
                other_url_params={
                }
            ),
        }
        return data

images_data_provider = ImagesDataProvider()
