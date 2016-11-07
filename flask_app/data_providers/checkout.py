#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from user_info import UserInfoDataProvider
from cart_table import CartTableDataProvider
from total_table import TotalTableDataProvider
from footer import FooterDataProvider

from flask import url_for

class CheckoutDataProvider():

	def get_data(self, step, in_edit_info_mode, user_email):
		return self.sample_data_0(step, in_edit_info_mode, user_email)

	def get_page_heading_data(self):
		return {
			"path": [
				{
					"name": "Home",
					"href": url_for("home"),
				},
				{
					"name": "Finalização de compra",
				},
			],
			"title": "Finalização de compra",
		}

	def sample_data_0(self, step, in_edit_info_mode, user_email):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": self.get_page_heading_data(),
			"footer_data": FooterDataProvider().get_data(),
			"step": step,
			"user_info_data": UserInfoDataProvider().get_data(in_edit_info_mode),
			"cart_table_data": CartTableDataProvider().get_fresh_order_data(user_email=user_email, editable=False),
			"total_table_data": TotalTableDataProvider().get_fresh_order_data(user_email=user_email),
		}
		return data