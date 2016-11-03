#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_redefine_password_data(form, email, msgs=[]):
	return sample_data_0(form=form, email=email, msgs=msgs)

def sample_data_0(form, email, msgs):
	data = {
		"header_data": get_header_data(),
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
		"msgs": msgs,
		"email": email,
		"form": form,
		"footer_data": get_footer_data(),
	}
	return data