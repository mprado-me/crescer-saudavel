#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider
from flask import url_for

class RecoverPasswordDataProvider():

	def get_data(self, form, msgs=[]):
		return self.sample_data_0(form=form, msgs=msgs)

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
						"name": "Entrar",
						"href": url_for("login"),
					},
					{
						"name": "Recuperar senha",
					},
				],
				"title": "Recuperar senha",
			},
			"msgs": msgs,
			"form": form,
			"footer_data": FooterDataProvider().get_data(),
		}
		return data