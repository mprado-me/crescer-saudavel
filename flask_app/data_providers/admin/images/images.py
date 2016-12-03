#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask_app.utils.utils import Utils
from flask_app import app

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNames

from flask_app.data_providers.shared.paginator import paginator_data_provider


class ImagesDataProvider:
    def __init__(self):
        pass

    def get_add_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.images),
            "form": form,
        }
        return data

    def get_data(self, page, remove_form, url_args):
        all_images_name = self.get_images_name_sorted()

        n_items = len(all_images_name)

        per_page = app.config["ADMIN_N_IMAGES_PER_PAGE"]

        range = Utils.get_page_range(page=page, n_items=n_items, per_page=per_page)
        sliced_images_name = all_images_name[range[0]:range[1]]

        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.images),
            "super_table_data": {
                "n_items": n_items,
                "paginator_data": paginator_data_provider.get_data(
                    page=page,
                    n_items=n_items,
                    per_page=per_page,
                    url_endpoint="admin_images",
                ),
                "table_data": self.get_table_data(
                    images_name=sliced_images_name,
                    remove_form=remove_form,
                    url_args=url_args
                ),
                "empty_msg": "Nenhuma imagem foi encontrada.",
            },
        }
        return data

    def get_images_name_sorted(self):
        all_images_name = os.listdir(app.config["UPLOADED_IMAGES_FOLDER"])
        all_images_name.sort()
        return all_images_name

    def get_table_data(self, images_name, remove_form, url_args):
        rows = []
        for idx, image_name in enumerate(images_name):
            rows.append([
                {
                    "file_path": "admin/images/image.html",
                    "data": {
                        "image_name": image_name
                    }
                },
                image_name,
                {
                    "file_path": "admin/images/actions.html",
                    "data": {
                        "image_name": image_name,
                        "remove_form": remove_form,
                        "row": idx,
                        "url_args": url_args
                    }
                }
            ])

        return {
            "id": "images-table",
            "cols": [
                {
                    "id": "image",
                    "type": "image"
                },
                {
                    "id": "image_name",
                    "title": "Nome",
                },
                {
                    "id": "actions",
                    "type": "actions",
                    "expandable": False,
                },
            ],
            "rows": rows,
        }


images_data_provider = ImagesDataProvider()
