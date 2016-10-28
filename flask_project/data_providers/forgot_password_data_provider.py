#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data
from flask import url_for

def get_forgot_password_data():
	return sample_data_0()

def sample_data_0():
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
					"href": url_for("login"),
				},
				{
					"name": "Recuperar senha",
				},
			],
			"title": "Recuperar senha",
		},
		"footer_data": get_footer_data(),
	}
	return data