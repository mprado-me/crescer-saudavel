#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from header import HeaderDataProvider
from cart_table import CartTableDataProvider
from total_table import TotalTableDataProvider
from footer import FooterDataProvider

class OrderDataProvider():

	def get_data(self, order_id):
		return self.sample_data_0(order_id)

	def get_page_heading_data(self, order_id):
		return {
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
		}

	def sample_data_0(self, order_id):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": self.get_page_heading_data(order_id),
			"cart_table_data": CartTableDataProvider().get_old_order_data(order_id=order_id),
			"total_table_data": TotalTableDataProvider().get_old_order_data(order_id=order_id),
			"footer_data": FooterDataProvider().get_data(),
		}
		return data