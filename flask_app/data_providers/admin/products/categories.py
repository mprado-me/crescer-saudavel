#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from sqlalchemy import asc

from flask_app.utils.utils import Utils
from flask_app import app

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNames

from flask_app.data_providers.shared.paginator import paginator_data_provider

from flask_app.models.category import Category

from flask_app.utils.db_manager import db_manager
from flask_app.utils.exceptions import InvalidParamError


class CategoriesDataProvider():
    def __init__(self):
        pass

    def get_add_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.products),
            "form": form,
        }
        return data

    def get_edit_data(self, form, category_id, url_args):
        category = db_manager.get_category(category_id=category_id)

        if not category:
            raise InvalidParamError(message="Category not found")

        form.category.data = category.name

        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.products),
            "form": form,
            "category_id": category_id,
            "url_args": url_args,
        }
        return data

    def get_data(self, page, simple_submit_form, filter_form, url_args, active):
        q = self.get_filtered_query(active=active)
        q = q.order_by(asc(Category.name))

        n_items = q.count()

        per_page = app.config["ADMIN_N_CATEGORIES_PER_PAGE"]

        filter_form.active.data = str(url_args["active"])

        return {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNames.products),
            "super_table_data": {
                "filter_data": {
                    "form": filter_form,
                    "action": url_for("admin_product_categories", **(Utils.new_merged_dic(url_args, {"page": 1}))),
                    "n_items": n_items
                },
                "paginator_data": paginator_data_provider.get_data(
                    page=page,
                    n_items=n_items,
                    per_page=per_page,
                    url_endpoint="admin_product_categories",
                    url_args=url_args
                ),
                "table_data": self.get_table_data(
                    categories=q.slice(*Utils.get_page_range(
                        page=page,
                        n_items=n_items,
                        per_page=per_page)).all(),
                    simple_submit_form=simple_submit_form
                ),
                "empty_msg": "Nenhuma categoria de produto foi encontrada.",
            },
        }

    def get_categories_sorted(self):
        return Category.query.order_by(Category.name).all()

    def get_table_data(self, categories, simple_submit_form):
        rows = []
        for idx, category in enumerate(categories):
            rows.append([
                "#" + str(category.id),
                category.active,
                category.name,
                {
                    "file_path": "admin/products/category_actions.html",
                    "data": {
                        "category_id": category.id,
                        "category_active": category.active,
                        "simple_submit_form": simple_submit_form,
                        "row": idx,
                    }
                }
            ])

        return {
            "id": "categories-table",
            "settings": {
                "vertical_align_middle": True,
            },
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
                    "id": "name",
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

    def get_filtered_query(self, active):
        q = Category.query

        q = q.filter(Category.active == active)

        return q


categories_data_provider = CategoriesDataProvider()
