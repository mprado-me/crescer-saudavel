#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_create_account_data(form):
	return sample_data_0(form)

def sample_data_0(form):
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
				},
			],
			"title": "Criar conta",
		},
		"form": form,
		"footer_data": get_footer_data(),
	}
	return data