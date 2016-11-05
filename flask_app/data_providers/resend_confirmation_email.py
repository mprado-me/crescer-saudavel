#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider

class ResendConfirmationEmailDataProvider():

	def get_data(self, form, msgs=[]):
		return self.sample_data_0(form, msgs)

	def sample_data_0(self, form, msgs):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
				"path": [
					{
						"name": "Home",
						"href": "/",
					},
					{
						"name": "Reenviar email de confirmação",
					},
				],
				"title": "Reenviar email de confirmação",
			},
			"msgs": msgs,
			"form": form,
			"footer_data": FooterDataProvider().get_data(),
		}
		return data