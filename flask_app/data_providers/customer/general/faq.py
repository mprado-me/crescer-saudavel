#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.customer.shared.footer import FooterDataProvider
from flask_app.data_providers.customer.shared.header import HeaderDataProvider

from flask import url_for


class FaqDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return self.sample_data_0()

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "FAQ",
                },
            ],
            "title": "FAQ",
        }

    def sample_data_0(self):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "footer_data": FooterDataProvider().get_data(),
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

faq_data_provider = FaqDataProvider()
