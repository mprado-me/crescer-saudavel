#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer_data_provider import get_footer_data
from flask import url_for

def get_forgot_password_email_sending_data():
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
					"name": "Entrar",
					"href": url_for("login"),
				},
				{
					"name": "Redefinir senha",
					"href": url_for("forgot_password"),
				},
				{
					"name": "Envio do email de redefinição de senha",
				},
			],
			"title": "Envio do email de redefinição de senha",
		},
		"email": "joao@gmail.com",
		"footer_data": get_footer_data(),
	}
	return data