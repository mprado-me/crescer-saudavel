#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider
from flask import url_for

class SentConfirmationEmailDataProvider():

	def get_data(self, email):
		return self.sample_data_0(email)

	def sample_data_0(self, email):
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
						"href": url_for("create_account"),
					},
					{
						"name": "Confirmação do email",
					},
				],
				"title": "Confirmação do email",
			},
			"email": email,
			"footer_data": FooterDataProvider().get_data(),
		}
		return data