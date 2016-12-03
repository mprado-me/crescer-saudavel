#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from flask_app import app

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNames

from flask_app.data_providers.shared.paginator import paginator_data_provider

from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory

from flask_app.utils.db_manager import db_manager
from flask_app.utils.exceptions import InvalidParamError

from flask import session

class SubcategoriesDataProvider():
    def __init__(self):
        pass

    def get_add_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.products),
            "form": form,
        }
        return data

    def get_edit_data(self, form, subcategory_id, url_args):
        subcategory = Subcategory.query.filter(Subcategory.id == subcategory_id).one_or_none()

        if not subcategory:
            raise InvalidParamError(message="Subcategory not found")

        form.subcategory.data = subcategory.name
        form.category_id.data = subcategory.category_id

        data = {
            "url_args": url_args,
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.products),
            "form": form,
            "subcategory_id": subcategory_id,
        }
        return data

    def get_data(self, page, remove_form, filter_category_form, category_id, url_args):
        subcategories = self.get_subcategories(category_id)

        empty = False
        if len(subcategories) == 0:
            empty = True

        total_n_pages = int(math.ceil(float(len(subcategories)) / app.config["DEFAULT_N_ITEMS_PER_PAGE"]))
        total_n_pages = max(1, total_n_pages)

        # page between 1 and total_n_pages
        page = max(1, page)
        page = min(total_n_pages, page)

        first = (page - 1) * app.config["DEFAULT_N_ITEMS_PER_PAGE"]
        last_plus_one = first + app.config["DEFAULT_N_ITEMS_PER_PAGE"]

        if category_id:
            filter_category_form.category_id.data = int(category_id)

        data = {
            "url_args": url_args,
            "remove_form": remove_form,
            "filter_category_form": filter_category_form,
            "empty": empty,
            "page": page,
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.products),
            "paginator_data": paginator_data_provider.get_data(
                page=page,
                n_pages=app.config["DEFAULT_PAGINATOR_SIZE"],
                total_n_pages=total_n_pages,
                url_endpoint="admin_product_subcategories",
                url_args={
                    "category_id": category_id,
                }
            ),
            "subcategories": subcategories[first:last_plus_one],
        }
        return data

    def get_subcategories(self, category_id):
        if category_id:
            return Subcategory.query.filter(Subcategory.category_id==category_id).order_by(Subcategory.name).all()
        else:
            return Subcategory.query.order_by(Subcategory.name).all()


subcategories_data_provider = SubcategoriesDataProvider()
