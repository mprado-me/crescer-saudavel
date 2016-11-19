#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from flask import url_for


class PaginatorDataProvider:
    def __init__(self):
        pass

    def get_data(self, current_page, n_pages, total_n_pages, url_endpoint, other_url_params=None):
        if other_url_params is None:
            other_url_params = {}

        pages_number = self.get_pages_number(current_page=current_page, n_pages=n_pages, total_n_pages=total_n_pages)
        pages = []
        url_params = {}

        for key, val in other_url_params.iteritems():
            url_params[key] = val

        for i in pages_number:
            url_params["page"] = i
            page = {
                "number": i,
                "href": url_for(url_endpoint, **url_params),
            }
            if i == current_page:
                page["active"] = True
            pages.append(
                page
            )

        previous_href = None
        next_href = None

        if pages_number[0] > 1:
            url_params["page"] = pages_number[0] - 1
            previous_href = url_for(url_endpoint, **url_params)
        if pages_number[-1] < total_n_pages:
            url_params["page"] = pages_number[-1] + 1
            next_href = url_for(url_endpoint, **url_params)

        return {
            "previous_href": previous_href,
            "next_href": next_href,
            "pages": pages,
        }

    def get_pages_number(self, current_page, n_pages, total_n_pages):
        first_page = int(math.floor((current_page - 1) / n_pages) * n_pages + 1)
        max_last_page = first_page + n_pages - 1
        last_page = min([total_n_pages, max_last_page])
        first_page = max([1, last_page - n_pages + 1])
        return range(first_page, (last_page + 1))

    def sample_data_0(self, current_page):
        data = {
            "next_href": url_for("all_products", page=5, sort_method=0),
            "pages": [
                {
                    "number": 1,
                    "href": url_for("all_products", page=1, sort_method=0),
                },
                {
                    "number": 2,
                    "href": url_for("all_products", page=2, sort_method=0),
                    "active": True,
                },
                {
                    "number": 3,
                    "href": url_for("all_products", page=3, sort_method=0),
                },
                {
                    "number": 4,
                    "href": url_for("all_products", page=4, sort_method=0),
                },
            ],
        }
        return data

paginator_data_provider = PaginatorDataProvider()
