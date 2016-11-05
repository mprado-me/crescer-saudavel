#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer_data_provider import get_footer_data

class CreateAccountDataProvider():

	def get_data(self, form, msg=None):
		return self.sample_data_0(form, msg)

	def sample_data_0(self, form, msg):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
				"path": [
					{
						"name": "Home",
						"href": "/",
					},
					{
						"name": "Criar conta",
					},
				],
				"title": "Criar conta",
			},
			"form": form,
			"msg": msg,
			"footer_data": get_footer_data(),
		}
		return data