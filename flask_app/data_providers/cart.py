#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider

class CartDataProvider():

	def get_data(self):
		return self.sample_data_0()

	def get_page_heading_data(self):
		return {
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
		}

	def sample_data_0(self):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": self.get_page_heading_data(),
			"footer_data": FooterDataProvider().get_data(),
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