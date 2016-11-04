#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_all_products_data(page, sort_method):
	return sample_data_0(page, sort_method)

def get_products_data_by_category(category_id, page, sort_method):
	return sample_data_0(page, sort_method)

def get_products_data_by_category_and_subcategory(category_id, subcategory_id, page, sort_method):
	return sample_data_0(page, sort_method, category_id, subcategory_id)

def get_products_data_by_search(page, sort_method, q):
	return sample_data_0(page, sort_method)

def sample_data_0(page, sort_method, category_id=None, subcategory_id=None):
	n_pages_in_paginator = 4
	data = {
		"header_data": get_header_data(),
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
		"footer_data": get_footer_data(),
	}
	return data