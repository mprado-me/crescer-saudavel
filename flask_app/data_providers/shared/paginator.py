#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from flask_app.utils.utils import Utils

from flask import url_for


class PaginatorDataProvider:
    def __init__(self):
        pass

    def get_data(self, page, n_items, per_page, paginator_size, url_endpoint, url_args=None):
        n_pages = Utils.get_n_pages(n_items=n_items, per_page=per_page)
        page = Utils.get_limited(value=page, min_limit=1, max_limit=n_pages)

        if url_args is None:
            url_args = {}

        pages_number = self.get_pages_number(page=page, paginator_size=paginator_size, n_pages=n_pages)
        pages = []
        url_params = {}

        for key, val in url_args.iteritems():
            url_params[key] = val

        for i in pages_number:
            url_params["page"] = i
            json_page = {
                "number": i,
                "href": url_for(url_endpoint, **url_params),
            }
            if i == page:
                json_page["active"] = True
            pages.append(json_page)

        previous_href = None
        next_href = None

        if pages_number[0] > 1:
            url_params["page"] = pages_number[0] - 1
            previous_href = url_for(url_endpoint, **url_params)
        if pages_number[-1] < n_pages:
            url_params["page"] = pages_number[-1] + 1
            next_href = url_for(url_endpoint, **url_params)

        return {
            "previous_href": previous_href,
            "next_href": next_href,
            "pages": pages,
        }

    def get_pages_number(self, page, paginator_size, n_pages):
        first_page = int(math.floor((page - 1) / paginator_size) * paginator_size + 1)
        max_last_page = first_page + paginator_size - 1
        last_page = min([n_pages, max_last_page])
        first_page = max([1, last_page - paginator_size + 1])
        return range(first_page, (last_page + 1))


paginator_data_provider = PaginatorDataProvider()
