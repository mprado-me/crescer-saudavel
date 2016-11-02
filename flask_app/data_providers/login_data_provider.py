#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_login_data(form, msgs=[]):
	return sample_data_0(form, msgs)

def sample_data_0(form, msgs):
	data = {
		"header_data": get_header_data(),
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
		"footer_data": get_footer_data(),
	}
	return data