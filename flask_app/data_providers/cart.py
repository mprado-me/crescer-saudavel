#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer_data_provider import get_footer_data

class CartDataProvider():

	def get_data(self):
		return self.sample_data_0()

	def sample_data_0(self):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
				"path": [
					{
						"name": "Home",
						"href": "/",
					},
					{
						"name": "Meu carrinho",
					},
				],
				"title": "Meu carrinho",
			},
			"footer_data": get_footer_data(),
			"cart_table_data": {
				"editable": True,
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
		}
		return data