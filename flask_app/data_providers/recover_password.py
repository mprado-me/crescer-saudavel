#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider
from flask import url_for

class RecoverPasswordDataProvider():

	def get_data(self, form, msgs=[]):
		return self.sample_data_0(form=form, msgs=msgs)

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
				},
			],
			"title": "Recuperar senha",
		}

	def sample_data_0(self, form, msgs):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": self.get_page_heading_data(),
			"msgs": msgs,
			"form": form,
			"footer_data": FooterDataProvider().get_data(),
		}
		return data