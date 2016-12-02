#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for

from flask_app import app
from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider
from flask_app.data_providers.shared.paginator import paginator_data_provider
from flask_app.utils.enums import ProductSortMethod

# For now, products data provider always return the data for products by category
class ProductsDataProvider:
    def __init__(self):
        pass

    def get_products_data(self, page, sort_method, category_id, subcategory_id):
        return self.sample_data_0(
            page=page,
            sort_method=sort_method,
            category_id=category_id,
            subcategory_id=subcategory_id)

    def get_page_heading_data_for_all_products(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Produtos",
                },
            ],
            "title": "Produtos",
        }

    def get_page_heading_data_for_products_by_category(self, page, sort_method, category_id):
        # TODO: Get category name from database
        category_name = "Categoria X"
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Produtos",
                    "href": url_for("products", page=page, sort_method=sort_method)
                },
                {
                    "name": category_name,
                },
            ],
            "title": category_name,
        }

    def get_page_heading_data_for_products_by_category_and_subcategory(self, page, sort_method, category_id, subcategory_id):
        # TODO: Get category name from database
        category_name = "Categoria X"
        # TODO: Get subcategory name from database
        subcategory_name = "Subcategoria Y"
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Produtos",
                    "href": url_for("products", page=page, sort_method=sort_method)
                },
                {
                    "name": category_name,
                    "href": url_for("products", page=page, sort_method=sort_method, category_id=category_id)
                },
                {
                    "name": subcategory_name,
                },
            ],
            "title": subcategory_name,
        }

    def get_products_data_by_search(self, page, q):
        # The line below is temporary
        return self.sample_data_0(page=page, sort_method=ProductSortMethod.NAME, category_id=1, subcategory_id=1)

    def get_page_heading_data_for_products_by_search(self, search_query):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Busca",
                },
            ],
            "title": search_query,
        }

    # Products by search doesn't have sort method options, the items are sorted based on the match with the query search parameter
    def get_sort_method_selector_data(self, name, sort_method_of_the_selector, page, sort_method, category_id, subcategory_id):
        active = sort_method_of_the_selector == sort_method
        href = None
        if not active:
            values = {
                "page": page,
                "sort_method": int(sort_method_of_the_selector),
            }
            if category_id:
                values["category_id"] = category_id
            if subcategory_id:
                values["subcategory_id"] = subcategory_id
            href = url_for("products", **values)
        return {
            "name": name,
            "active": active,
            "href": href,
        }

    def sample_data_0(self, page, sort_method, category_id, subcategory_id):
        data = {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data_for_products_by_category(
                category_id=category_id,
                page=page,
                sort_method=sort_method),
            "sort_method_selectors": [
                self.get_sort_method_selector_data(
                    name="Nome",
                    sort_method_of_the_selector=ProductSortMethod.NAME,
                    page = page,
                    sort_method=sort_method,
                    category_id=category_id,
                    subcategory_id=subcategory_id,
                ),
                self.get_sort_method_selector_data(
                    name="Menor preço",
                    sort_method_of_the_selector=ProductSortMethod.LOWEST_PRICE,
                    page=page,
                    sort_method=sort_method,
                    category_id=category_id,
                    subcategory_id=subcategory_id,
                ),
                self.get_sort_method_selector_data(
                    name="Maior preço",
                    sort_method_of_the_selector=ProductSortMethod.BIGGEST_PRICE,
                    page=page,
                    sort_method=sort_method,
                    category_id=category_id,
                    subcategory_id=subcategory_id,
                ),
                self.get_sort_method_selector_data(
                    name="Mais vendido",
                    sort_method_of_the_selector=ProductSortMethod.BEST_SELLER,
                    page=page,
                    sort_method=sort_method,
                    category_id=category_id,
                    subcategory_id=subcategory_id,
                ),
            ],
            "paginator_data": paginator_data_provider.get_data(
                page=page,
                n_pages=app.config["USER_PRODUCTS_PAGINATOR_SIZE"],
                total_n_pages=10,
                url_endpoint="products",
                url_args={
                    "sort_method": sort_method,
                }
            ),
            "products": [
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
                {
                    "title": "Nome do produto",
                    "product_id": 0,
                    "href": url_for("product", product_id=0),
                    "img_src": url_for("static", filename="images/products/p1.jpg"),
                    "price": "R$ 0,00",
                },
            ],
            "footer_data": footer_data_provider.get_data(),
        }
        return data

products_data_provider = ProductsDataProvider()
