#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header import HeaderDataProvider
from footer_data_provider import get_footer_data

class GetFailDataProvider():

	def get_data(self, msg, button):
		return self.sample_data_0(msg, button)

	def sample_data_0(self, msg, button):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
				"title": "Falha",
			},
			"msg": msg,
			"button": button,
			"footer_data": get_footer_data(),
		}
		return data