#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_create_account_data(form, msg=None):
	return sample_data_0(form, msg)

def sample_data_0(form, msg):
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
		"msg": msg,
		"footer_data": get_footer_data(),
	}
	return data