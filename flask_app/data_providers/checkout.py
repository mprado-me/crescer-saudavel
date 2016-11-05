#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer_data_provider import get_footer_data
from user_info_data_provider import get_user_info_data

class CheckoutDataProvider():

	def get_data(self, step, in_edit_info_mode):
		return self.sample_data_0(step, in_edit_info_mode)

	def sample_data_0(self, step, in_edit_info_mode):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
				"path": [
					{
						"name": "Home",
						"href": "/",
					},
					{
						"name": "Finalização de compra",
					},
				],
				"title": "Finalização de compra",
			},
			"footer_data": get_footer_data(),
			"step": step,
			"user_info_data": get_user_info_data(in_edit_info_mode),
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
		}
		return data