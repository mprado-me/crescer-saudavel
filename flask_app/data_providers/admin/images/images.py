#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, math

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
        all_images_name = self.get_images_name(page=page)
        all_images_name.sort()

        empty = False
        if len(all_images_name) == 0:
            empty = True

        total_n_pages = int(math.ceil(float(len(all_images_name))/app.config["N_ITEMS_BY_PAGE_IN_ADMIN_IMAGES"]))
        total_n_pages = max(1, total_n_pages)

        first = (page-1)*app.config["N_ITEMS_BY_PAGE_IN_ADMIN_IMAGES"]
        last_plus_one = first+app.config["N_ITEMS_BY_PAGE_IN_ADMIN_IMAGES"]

        data = {
            "empty": empty,
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.images),
            "paginator_data": paginator_data_provider.get_data(
                current_page=page,
                n_pages=app.config["N_PAGES_IN_ADMIN_IMAGES"],
                total_n_pages=total_n_pages,
                url_endpoint="admin_images",
                other_url_params={
                }
            ),
            "images_name": all_images_name[first:last_plus_one],
        }
        return data

    def get_images_name(self, page):
        return os.listdir(app.config["UPLOADED_IMAGES_FOLDER"])


images_data_provider = ImagesDataProvider()
