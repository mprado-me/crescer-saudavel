#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, math

from flask_app import app

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask_app.data_providers.shared.paginator import paginator_data_provider


class ImagesDataProvider:
    def __init__(self):
        pass

    def get_add_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.images),
            "form": form,
        }
        return data

    def get_data(self, page, remove_form, url_args):
        all_images_name = self.get_images_name_sorted()

        empty = False
        if len(all_images_name) == 0:
            empty = True

        total_n_pages = int(math.ceil(float(len(all_images_name))/app.config["ADMIN_N_IMAGES_PER_PAGE"]))
        total_n_pages = max(1, total_n_pages)

        # page between 1 and total_n_pages
        page = max(1, page)
        page = min(total_n_pages, page)

        first = (page-1)*app.config["ADMIN_N_IMAGES_PER_PAGE"]
        last_plus_one = first+app.config["ADMIN_N_IMAGES_PER_PAGE"]

        data = {
            "url_args": url_args,
            "remove_form": remove_form,
            "empty": empty,
            "page": page,
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.images),
            "paginator_data": paginator_data_provider.get_data(
                page=page,
                n_pages=app.config["ADMIN_IMAGES_TABLE_PAGINATOR_SIZE"],
                total_n_pages=total_n_pages,
                url_endpoint="admin_images",
                url_args={
                }
            ),
            "images_name": all_images_name[first:last_plus_one],
        }
        return data

    def get_images_name_sorted(self):
        all_images_name = os.listdir(app.config["UPLOADED_IMAGES_FOLDER"])
        all_images_name.sort()
        return all_images_name


images_data_provider = ImagesDataProvider()
