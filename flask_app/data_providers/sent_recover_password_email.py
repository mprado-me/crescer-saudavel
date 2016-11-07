#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for

from header import HeaderDataProvider
from footer import FooterDataProvider

class SentRecoverPasswordEmailDataProvider():

	def get_data(self, email):
		return self.sample_data_0(email=email)

	def get_page_heading_data(self):
		return {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Entrar",
					"href": url_for("login"),
				},
				{
					"name": "Recuperar senha",
					"href": url_for("recover_password"),
				},
				{
					"name": "Envio do email de recuperação de senha",
				},
			],
			"title": "Envio do email de recuperação de senha",
		}

	def sample_data_0(self, email):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": self.get_page_heading_data(),
			"email": email,
			"footer_data": FooterDataProvider().get_data(),
		}
		return data