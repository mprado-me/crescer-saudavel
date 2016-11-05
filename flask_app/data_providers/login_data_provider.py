#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider

def get_login_data(form, msgs=[]):
	return sample_data_0(form, msgs)

def sample_data_0(form, msgs):
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
				},
			],
			"title": "Entrar",
		},
		"msgs": msgs,
		"form": form,
		"footer_data": FooterDataProvider().get_data(),
	}
	return data