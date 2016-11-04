#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from header_data_provider import get_header_data
from footer_data_provider import get_footer_data
from user_info_data_provider import get_user_info_data

def get_my_account_data(editable):
	return sample_data_1(editable)

def sample_data_0(editable):
	data = {
		"header_data": get_header_data(),
		"page_heading_data": {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Minha conta",
				},
			],
			"title": "Minha conta",
		},
		"user_info_data": get_user_info_data(editable),
		"orders": [
			{
				"id": 123,
				"date": "05/12/2015",
				"total": "R$ 125,00",
				"status": "Empacotando",
			},
			{
				"id": 12312,
				"date": "05/11/2015",
				"total": "R$ 65,00",
				"status": "Enviado",
			},
			{
				"id": 1213,
				"date": "05/10/2015",
				"total": "R$ 25,00",
				"status": "Entregue",
			},
		],
		"footer_data": get_footer_data(),
	}
	return data

def sample_data_1(editable):
	data = {
		"header_data": get_header_data(),
		"page_heading_data": {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Minha conta",
				},
			],
			"title": "Minha conta",
		},
		"user_info_data": get_user_info_data(editable),
		"orders": [],
		"footer_data": get_footer_data(),
	}
	return data