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


class ProductsDataProvider():
    def __init__(self):
        pass

    def get_add_data(self, form):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "form": form,
        }
        return data

    def get_edit_data(self, form, product_id):
        product = db_manager.get_product(product_id=product_id)

        if not product:
            raise InvalidParamError()

        form.title.data = product.title
        form.category_subcategory.data = str(product.category_id) + "/" + str(product.subcategory_id)
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
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.products),
            "form": form,
            "product_id": product_id,
        }
        return data

products_data_provider = ProductsDataProvider()
