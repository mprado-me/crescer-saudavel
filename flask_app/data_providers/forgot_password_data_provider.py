#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data
from flask import url_for

def get_forgot_password_data(form, msgs=[]):
	return sample_data_0(form=form, msgs=msgs)

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
					"href": url_for("login"),
				},
				{
					"name": "Redefinir senha",
				},
			],
			"title": "Redefinir senha",
		},
		"msgs": msgs,
		"form": form,
		"footer_data": get_footer_data(),
	}
	return data