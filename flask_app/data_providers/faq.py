#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer_data_provider import get_footer_data

class FaqDataProvider():

	def get_data(self):
		return self.sample_data_0()

	def sample_data_0(self):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
				"path": [
					{
						"name": "Home",
						"href": "/",
					},
					{
						"name": "FAQ",
					},
				],
				"title": "FAQ",
			},
			"footer_data": get_footer_data(),
			"perguntas_e_respostas": [
				{
					"pergunta": "Essa é a pergunta 1?",
					"resposta": "Essa é a resposta a pergunta 1"
				},
				{
					"pergunta": "Essa é a pergunta 2?",
					"resposta": "Essa é a resposta a pergunta 2"
				},
				{
					"pergunta": "Essa é a pergunta 3?",
					"resposta": "Essa é a resposta a pergunta 3"
				},
				{
					"pergunta": "Essa é a pergunta 4?",
					"resposta": "Essa é a resposta a pergunta 4"
				}
			]
		}
		return data