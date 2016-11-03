#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_redefine_password_data(form, email, token, msgs=[]):
	return sample_data_0(form=form, email=email, token=token, msgs=msgs)

def sample_data_0(form, email, token, msgs):
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
		"token": token,
		"msgs": msgs,
		"email": email,
		"form": form,
		"footer_data": get_footer_data(),
	}
	return data