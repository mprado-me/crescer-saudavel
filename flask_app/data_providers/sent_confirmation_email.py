#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data
from flask import url_for

class SentConfirmationEmailDataProvider():

	def get_data(self, email):
		return self.sample_data_0(email)

	def sample_data_0(self, email):
		data = {
			"header_data": get_header_data(),
			"page_heading_data": {
				"path": [
					{
						"name": "Home",
						"href": "/",
					},
					{
						"name": "Criar conta",
						"href": url_for("create_account"),
					},
					{
						"name": "Confirmação do email",
					},
				],
				"title": "Confirmação do email",
			},
			"email": email,
			"footer_data": get_footer_data(),
		}
		return data