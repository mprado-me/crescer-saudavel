#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_order_data(order_id):
	return sample_data_0(order_id)

def sample_data_0(order_id):
	data = {
		"header_data": get_header_data(),
		"page_heading_data": {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Minha conta",
					"href": url_for('my_account'),
				},
				{
					"name": "Pedido",
				},
			],
			"title": "Pedido #" + str(order_id),
		},
		"cart_table_data": {
			"editable": False,
			"products": [
				{
					"id": 1,
					"image_href": "/static/images/products/p8.jpg",
					"title": "Papinha de maça - 500g",
					"unit_price": "R$ 10,00",
					"quantity": 2,
					"subtotal": "R$ 20,00",
				},
				{
					"id": 2,
					"image_href": "/static/images/products/p8.jpg",
					"title": "Papinha de arroz doce - 200g",
					"unit_price": "R$ 4,20",
					"quantity": 3,
					"subtotal": "R$ 12,60",
				},
			],
		},
		"total_table_data": {
			"products_total": "R$ 32,60",
			"frete": "R$ 5,00",
			"total": "R$ 37,60",
		},
		"footer_data": get_footer_data(),
	}
	return data