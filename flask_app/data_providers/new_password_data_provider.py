#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider

def get_new_password_data():
	return sample_data_0()

def sample_data_0():
	data = {
		"header_data": HeaderDataProvider().get_data(),
		"page_heading_data": {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Definir nova senha",
				},
			],
			"title": "Definir nova senha",
		},
		"footer_data": FooterDataProvider().get_data(),
	}
	return data