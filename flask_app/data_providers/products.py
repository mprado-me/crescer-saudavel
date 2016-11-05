#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from header import HeaderDataProvider
from footer import FooterDataProvider

class ProductsDataProvider():

	def get_all_products_data(self, page, sort_method):
		return self.sample_data_0(page, sort_method)

	def get_products_data_by_category(self, category_id, page, sort_method):
		return self.sample_data_0(page, sort_method)

	def get_products_data_by_category_and_subcategory(self, category_id, subcategory_id, page, sort_method):
		return self.sample_data_0(page, sort_method, category_id, subcategory_id)

	def get_products_data_by_search(self, page, sort_method, q):
		return self.sample_data_0(page, sort_method)

	def sample_data_0(self, page, sort_method, category_id=0, subcategory_id=0):
		n_pages_in_paginator = 4
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
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
			},
			"route": {
				"handler_func": "products_by_category_and_subcategory",
				"category_id": category_id,
				"subcategory_id": subcategory_id,
			},
			"sort_method": sort_method,
			"paginator_data": {
				"next_href": url_for("all_products", page=5, sort_method=0),
				"pages": [
					{
						"number": 1,
						"href": url_for("all_products", page=1, sort_method=0),
					},
					{
						"number": 2,
						"href": url_for("all_products", page=2, sort_method=0),
						"active": True,
					},
					{
						"number": 3,
						"href": url_for("all_products", page=3, sort_method=0),
					},
					{
						"number": 4,
						"href": url_for("all_products", page=4, sort_method=0),
					},
				],
			},
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