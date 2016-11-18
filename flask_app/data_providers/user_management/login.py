#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, url_for

from flask_app.data_providers.shared.footer import FooterDataProvider
from flask_app.data_providers.shared.header import HeaderDataProvider
from flask_app.utils.exceptions import DatabaseAccessError


class LoginDataProvider:
    def __init__(self):
        pass

    def get_data(self, form):
        return self.sample_data_0(form=form)

    def get_data_when_get_request(self, form):
        data = self.get_data(form=form)
        msgs = []
        msg_content = request.args.get("msg_content")
        msg_type = request.args.get("msg_type")
        if msg_content and msg_type:
            msgs.append({
                "type": msg_type,
                "content": msg_content,
            })
        data["msgs"] = msgs
        return data

    def get_data_when_database_access_error(self, form):
        data = self.get_data(form=form)
        msgs = [DatabaseAccessError.msg]
        data["msgs"] = msgs
        return data

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Entrar",
                },
            ],
            "title": "Entrar",
        }

    def sample_data_0(self, form):
        data = {
            "header_data": HeaderDataProvider().get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "form": form,
            "footer_data": FooterDataProvider().get_data(),
        }
        return data

login_data_provider = LoginDataProvider()