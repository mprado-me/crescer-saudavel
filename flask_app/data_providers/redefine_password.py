#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider

class RedefinePasswordData():

	def get_data(self, form, email, token, msgs=[]):
		return self.sample_data_0(form=form, email=email, token=token, msgs=msgs)

	def sample_data_0(self, form, email, token, msgs):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
				"path": [
					{
						"name": "Home",
						"href": "/",
					},
					{
						"name": "Redefinir senha",
					},
				],
				"title": "Redefinir senha",
			},
			"token": token,
			"msgs": msgs,
			"email": email,
			"form": form,
			"footer_data": FooterDataProvider().get_data(),
		}
		return data