#!/usr/bin/env python
# -*- coding: utf-8 -*-

from footer_data_provider import get_footer_data

def get_login_data(finalizando_compra):
	return sample_data_0(finalizando_compra)

def sample_data_0(finalizando_compra):
	data = {
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
		"footer_data": get_footer_data(),
		"finalizando_compra": finalizando_compra
	}
	return data