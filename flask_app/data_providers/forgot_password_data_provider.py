#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer import FooterDataProvider
from flask import url_for

def get_forgot_password_data(form, msgs=[]):
	return sample_data_0(form=form, msgs=msgs)

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
		"footer_data": FooterDataProvider().get_data(),
	}
	return data