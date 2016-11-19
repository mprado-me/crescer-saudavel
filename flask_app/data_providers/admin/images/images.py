#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.admin.shared.navbar import navbar_data_provider
from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask import request


class ImagesDataProvider:
    def __init__(self):
        pass

    def get_data(self, page):
        return self.sample_data_0(page=page)

    def get_data_with_request_msg(self, page):
        data = self.get_data(page=page)
        msgs = []
        msg_content = request.args.get("msg_content")
        msg_type = request.args.get("msg_type")
        if msg_content and msg_type:
            msgs.append({
                "type": msg_type,
                "content": msg_content,
            })
        if "msgs" in data:
            data["msgs"] = data["msgs"] + msgs
        else:
            data["msgs"] = msgs
        return data

    def sample_data_0(self, page):
        data = {
            "navbar_data": navbar_data_provider.get_data(active_tab_name=NavbarTabNamesProvider.images),
        }
        return data

images_data_provider = ImagesDataProvider()
