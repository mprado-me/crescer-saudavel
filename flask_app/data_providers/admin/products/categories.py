#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from flask_app import app

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask_app.data_providers.shared.paginator import paginator_data_provider

from flask_app.models.category import Category

from flask_app.utils.db_manager import db_manager
from flask_app.utils.exceptions import InvalidParamError


class CategoriesDataProvider():
    def __init__(self):
        pass

    def get_add_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "form": form,
        }
        return data

    def get_edit_data(self, form, category_id, page_to_return):
        category = db_manager.get_category(category_id=category_id)

        if not category:
            raise InvalidParamError(message="Category not found")

        form.category.data = category.name

        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "form": form,
            "category_id": category_id,
            "page_to_return": page_to_return,
        }
        return data

    def get_data(self, page, remove_form):
        all_categories = self.get_categories_sorted()

        empty = False
        if len(all_categories) == 0:
            empty = True

        total_n_pages = int(math.ceil(float(len(all_categories)) / app.config["DEFAULT_N_ITEMS_BY_PAGE"]))
        total_n_pages = max(1, total_n_pages)

        # page between 1 and total_n_pages
        page = max(1, page)
        page = min(total_n_pages, page)

        first = (page - 1) * app.config["DEFAULT_N_ITEMS_BY_PAGE"]
        last_plus_one = first + app.config["DEFAULT_N_ITEMS_BY_PAGE"]

        data = {
            "remove_form": remove_form,
            "empty": empty,
            "page": page,
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "paginator_data": paginator_data_provider.get_data(
                current_page=page,
                n_pages=app.config["DEFAULT_N_PAGES_IN_PAGINATOR"],
                total_n_pages=total_n_pages,
                url_endpoint="admin_product_categories",
                other_url_params={
                }
            ),
            "categories": all_categories[first:last_plus_one],
        }
        return data

    def get_categories_sorted(self):
        return Category.query.order_by(Category.name).all()


categories_data_provider = CategoriesDataProvider()
