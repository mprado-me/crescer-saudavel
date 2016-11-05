#!/usr/bin/env python
# -*- coding: utf-8 -*-

from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

class GetFailDataProvider():

	def get_data(self, msg, button):
		return self.sample_data_0(msg, button)

	def sample_data_0(self, msg, button):
		data = {
			"header_data": get_header_data(),
			"page_heading_data": {
				"title": "Falha",
			},
			"msg": msg,
			"button": button,
			"footer_data": get_footer_data(),
		}
		return data