#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from flask_app import app

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask_app.data_providers.shared.paginator import paginator_data_provider

from flask_app.models.product import Product

from flask_app.utils.db_manager import db_manager
from flask_app.utils.enums import AdminProductsTableSortMethod
from flask_app.utils.exceptions import InvalidParamError
from flask_app.utils.string import String
from flask_app.utils.utils import Utils

from flask import url_for

from sqlalchemy import asc, desc


class ProductsDataProvider():
    def __init__(self):
        pass

    def get_add_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "form": form,
        }
        return data

    def get_edit_data(self, form, product_id, url_args):
        product = db_manager.get_product(product_id=product_id)

        if not product:
            raise InvalidParamError()

        category_id = product.category_id
        if not category_id:
            category_id = 0
        subcategory_id = product.subcategory_id
        if not subcategory_id:
            subcategory_id = 0

        form.title.data = product.title
        form.category_subcategory.data = str(category_id) + "/" + str(subcategory_id)
        form.price.data = str(product.price)
        form.stock_quantity.data = str(product.stock_quantity)
        form.stop_sell_stock_quantity.data = str(product.stop_sell_stock_quantity)
        form.summary.data = product.summary

        form.image_1.data = product.image_1
        form.image_2.data = product.image_2
        form.image_3.data = product.image_3
        form.image_4.data = product.image_4
        form.image_5.data = product.image_5
        form.image_6.data = product.image_6
        form.image_7.data = product.image_7
        form.image_8.data = product.image_8
        form.image_9.data = product.image_9
        form.image_10.data = product.image_10

        form.tab_1_title.data = product.tab_1_title
        form.tab_1_content.data = product.tab_1_content
        form.tab_2_title.data = product.tab_2_title
        form.tab_2_content.data = product.tab_2_content
        form.tab_3_title.data = product.tab_3_title
        form.tab_3_content.data = product.tab_3_content
        form.tab_4_title.data = product.tab_4_title
        form.tab_4_content.data = product.tab_4_content
        form.tab_5_title.data = product.tab_5_title
        form.tab_5_content.data = product.tab_5_content
        form.tab_6_title.data = product.tab_6_title
        form.tab_6_content.data = product.tab_6_content
        form.tab_7_title.data = product.tab_7_title
        form.tab_7_content.data = product.tab_7_content
        form.tab_8_title.data = product.tab_8_title
        form.tab_8_content.data = product.tab_8_content
        form.tab_9_title.data = product.tab_9_title
        form.tab_9_content.data = product.tab_9_content
        form.tab_10_title.data = product.tab_10_title
        form.tab_10_content.data = product.tab_10_content

        data = {
            "url_args": url_args,
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "form": form,
            "product_id": product_id,
        }
        return data

    def get_data(self, page, simple_submit_form, stock_operation_form, filter_product_form, category_id, subcategory_id,
                 active, category_subcategory, url_args, selected_sort_method):
        q = self.get_filtered_query(category_id=category_id, subcategory_id=subcategory_id, active=active)
        q = q.order_by(self.get_order_by_arg(sort_method=selected_sort_method))

        n_items = q.count()

        filter_product_form.category_subcategory.data = category_subcategory
        filter_product_form.active.data = str(active)

        return {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "super_table_data": {
                "filter_data": {
                    "form": filter_product_form,
                    "action": url_for("admin_products", **(Utils.new_dic(url_args, {"page": 1})))
                },
                "paginator_data": paginator_data_provider.get_data(
                    page=page,
                    n_items=n_items,
                    per_page=app.config["ADMIN_N_PRODUCTS_PER_PAGE"],
                    url_endpoint="admin_products",
                    url_args=url_args),
                "sort_method_query_arg_name": String.QueryArgName.SORT_METHOD,
                "sort_methods": [
                    self.get_sort_method(selected_sort_method, "Título",
                                         int(AdminProductsTableSortMethod.TITLE)),
                    self.get_sort_method(selected_sort_method, "Menor preço",
                                         int(AdminProductsTableSortMethod.LOWEST_PRICE)),
                    self.get_sort_method(selected_sort_method, "Maior preço",
                                         int(AdminProductsTableSortMethod.BIGGEST_PRICE)),
                    self.get_sort_method(selected_sort_method, "Menor estoque",
                                         int(AdminProductsTableSortMethod.LOWEST_STOCK)),
                    self.get_sort_method(selected_sort_method, "Maior estoque",
                                         int(AdminProductsTableSortMethod.HIGHER_STOCK)),
                    self.get_sort_method(selected_sort_method, "Mais vendido",
                                         int(AdminProductsTableSortMethod.BEST_SELLER)),
                    self.get_sort_method(selected_sort_method, "Menos vendido",
                                         int(AdminProductsTableSortMethod.LESS_SOLD)),
                ],
                "table_data": self.get_table_data(
                    products=q.slice(*Utils.get_page_range(page=page,
                                                          n_items=n_items,
                                                          per_page=app.config["ADMIN_N_PRODUCTS_PER_PAGE"])).all(),
                    url_args=url_args,
                    simple_submit_form=simple_submit_form,
                    stock_operation_form=stock_operation_form),
                "empty_msg": "Nenhum produto foi encontrado.",
            }
        }

    def get_filtered_query(self, category_id, subcategory_id, active):
        q = Product.query

        if category_id:
            q = q.filter(Product.category_id == category_id)
        if category_id and subcategory_id:
            q = q.filter(Product.subcategory_id == subcategory_id)

        q = q.filter(Product.active == active)

        return q

    def get_order_by_arg(self, sort_method):
        if sort_method == int(AdminProductsTableSortMethod.TITLE):
            return asc(Product.title)
        elif sort_method == int(AdminProductsTableSortMethod.LOWEST_PRICE):
            return asc(Product.price)
        elif sort_method == int(AdminProductsTableSortMethod.BIGGEST_PRICE):
            return desc(Product.price)
        elif sort_method == int(AdminProductsTableSortMethod.LOWEST_STOCK):
            return asc(Product.stock)
        elif sort_method == int(AdminProductsTableSortMethod.HIGHER_STOCK):
            return desc(Product.stock)
        elif sort_method == int(AdminProductsTableSortMethod.BEST_SELLER):
            return desc(Product.sales_number)
        elif sort_method == int(AdminProductsTableSortMethod.LESS_SOLD):
            return asc(Product.sales_number)

    def get_table_data(self, products, url_args, simple_submit_form, stock_operation_form):
        rows = []
        for idx, product in enumerate(products):
            rows.append([
                "#" + str(product.id),
                product.active,
                product.category.name if product.category else "-",
                product.subcategory.name if product.subcategory else "-",
                product.title,
                product.price,
                product.stock,
                product.min_stock,
                product.sales_number,
                {
                    "product_id": product.id,
                    "product_active": product.active,
                    "row": idx,
                    "file": url_for("static", filename="templates/admin/actions.html"),
                    "url_args": url_args,
                    "simple_submit_form": simple_submit_form,
                    "stock_operation_form": stock_operation_form,
                }
            ])

        return {
            "cols": [
                {
                    "id": "id",
                    "title": "Id",
                },
                {
                    "id": "active",
                    "title": "Ativo",
                    "showAsBool": True
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
                    "id": "title",
                    "title": "Título",
                },
                {
                    "id": "price",
                    "title": "Preço",
                },
                {
                    "id": "stock",
                    "title": "Em estoque",
                },
                {
                    "id": "min_stock",
                    "title": "Mín. estoque",
                    "tooltip": "Quando o estoque do produto for menor ou igual ao valor estabelecido, o produto não será mais disponibilizado para venda no site."
                },
                {
                    "id": "sales_number",
                    "title": "Vendas",
                    "tooltip": "Total de vendas do produto pelo site."
                },
                {
                    "id": "actions",
                },
            ],
            "rows": rows,
        }

    def get_sort_method(self, selected_sort_method, name, sort_method):
        return {
            "name": name,
            "value": sort_method,
            "selected": sort_method == selected_sort_method
        }


products_data_provider = ProductsDataProvider()
