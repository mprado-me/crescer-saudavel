#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from header import HeaderDataProvider
from footer import FooterDataProvider
from paginator import PaginatorDataProvider
from .. import app

class ProductsDataProvider():

	def get_all_products_data(self, page, sort_method):
		return self.sample_data_0(page, sort_method)

	def get_page_heading_data_for_all_products(self):
		return {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Produtos",
				},
			],
			"title": "Produtos",
		}

	def get_products_data_by_category(self, category_id, page, sort_method):
		return self.sample_data_0(page, sort_method)

	def get_page_heading_data_for_products_by_category(self, category_id, page, sort_method):
		# TODO: Get category name from database
		category_name = "Categoria X"
		return {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Produtos",
					"href": url_for("all_products", page=page, sort_method=sort_method)
				},
				{
					"name": category_name,
				},
			],
			"title": "category_name",
		}

	def get_products_data_by_category_and_subcategory(self, category_id, subcategory_id, page, sort_method):
		return self.sample_data_0(page, sort_method, category_id, subcategory_id)

	def get_page_heading_data_for_products_by_category_and_subcategory(self, category_id, subcategory_id, page, sort_method):
		# TODO: Get category name from database
		category_name = "Categoria X"
		# TODO: Get subcategory name from database
		subcategory_name = "Subcategoria Y"
		return {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Produtos",
					"href": url_for("all_products", page=page, sort_method=sort_method)
				},
				{
					"name": category_name,
					"href": url_for("products_by_category", category_id=category_id, page=page, sort_method=sort_method)
				},
				{
					"name": subcategory_name,
				},
			],
			"title": "Produtos",
		}

	def get_products_data_by_search(self, page, sort_method, q):
		return self.sample_data_0(page, sort_method)

	def get_page_heading_data_for_products_by_search(self, search_query):
		return {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Busca",
				},
			],
			"title": search_query,
		}

	def sample_data_0(self, page, sort_method, category_id=0, subcategory_id=0):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": self.get_page_heading_data_for_products_by_category(category_id=category_id, page=page, sort_method=sort_method),
			"route": {
				"handler_func": "products_by_category_and_subcategory",
				"category_id": category_id,
				"subcategory_id": subcategory_id,
			},
			"sort_method": sort_method,
			"paginator_data": PaginatorDataProvider().get_data(
				current_page=page,
				n_pages=app.config["N_PAGES_IN_PRODUCTS_PAGINATOR"],
				total_n_pages=10,
				url_endpoint="products_by_category",
				other_url_params = {
					"sort_method": 0,
					"category_id": 0,
				}
			),
			"products": [
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
				{
					"title": "Nome do produto",
					"product_id": 0,
					"href": url_for("product", product_id=0),
					"img_src": "/static/images/products/p1.jpg",
					"price": "R$ 0,00",
				},
			],
			"footer_data": FooterDataProvider().get_data(),
		}
		return data