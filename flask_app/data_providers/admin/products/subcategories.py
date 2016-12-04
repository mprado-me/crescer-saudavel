#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from flask import url_for
from sqlalchemy import asc

from flask_app.utils.utils import Utils
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

    def get_data(self, page, simple_submit_form, filter_subcategory_form, category_id, active, url_args):
        q = self.get_filtered_query(category_id=category_id, active=active)
        q = q.order_by(asc(Subcategory.name))

        n_items = q.count()

        filter_subcategory_form.category_id.data = int(category_id)
        filter_subcategory_form.active.data = str(active)

        per_page = app.config["ADMIN_N_SUBCATEGORIES_PER_PAGE"]

        return {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.products),
            "super_table_data": {
                "filter_data": {
                    "form": filter_subcategory_form,
                    "action": url_for("admin_product_subcategories", **(Utils.new_merged_dic(url_args, {"page": 1}))),
                    "n_items": n_items
                },
                "paginator_data": paginator_data_provider.get_data(
                    page=page,
                    n_items=n_items,
                    per_page=per_page,
                    url_endpoint="admin_product_subcategories",
                    url_args=url_args),
                "table_data": self.get_table_data(
                    subcategories=q.slice(*Utils.get_page_range(page=page,
                                                           n_items=n_items,
                                                           per_page=per_page)).all(),
                    url_args=url_args,
                    simple_submit_form=simple_submit_form),
                "empty_msg": "Nenhuma subcategoria foi encontrada.",
            }
        }

    def get_subcategories(self, category_id):
        if category_id:
            return Subcategory.query.filter(Subcategory.category_id==category_id).order_by(Subcategory.name).all()
        else:
            return Subcategory.query.order_by(Subcategory.name).all()

    def get_filtered_query(self, category_id, active):
        q = Subcategory.query

        if category_id != 0:
            q = q.filter(Subcategory.category_id == category_id)

        q = q.filter(Subcategory.active == active)

        return q

    def get_table_data(self, subcategories, url_args, simple_submit_form):
        rows = []
        for idx, subcategory in enumerate(subcategories):
            rows.append([
                "#" + str(subcategory.id),
                subcategory.active,
                subcategory.category.name if subcategory.category else "-",
                subcategory.name,
                {
                    "file_path": "admin/products/subcategory_actions.html",
                    "data": {
                        "subcategory_id": subcategory.id,
                        "subcategory_active": subcategory.active,
                        "row": idx,
                        "url_args": url_args,
                        "simple_submit_form": simple_submit_form,
                    }
                }
            ])

        return {
            "id": "products-table",
            "cols": [
                {
                    "id": "id",
                    "title": "Id",
                },
                {
                    "id": "active",
                    "title": "Ativa",
                    "type": "bool"
                },
                {
                    "id": "category",
                    "title": "Categoria",
                },
                {
                    "id": "subcategory",
                    "title": "Subcategoria",
                },
                {
                    "id": "actions",
                    "type": "actions",
                },
            ],
            "rows": rows,
        }


subcategories_data_provider = SubcategoriesDataProvider()
