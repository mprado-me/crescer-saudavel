#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from flask_app.utils.utils import Utils

from flask import url_for


class PaginatorDataProvider:
    def __init__(self):
        pass

    def get_data(self, page, n_items, per_page, url_endpoint, url_args=None):
        n_pages = Utils.get_n_pages(n_items=n_items, per_page=per_page)
        page = Utils.get_limited(value=page, min_limit=1, max_limit=n_pages)

        if url_args is None:
            url_args = {}

        pages = self.get_pages(page=page, n_pages=n_pages, url_endpoint=url_endpoint, url_args=url_args)

        previous_href = None
        next_href = None

        if n_pages > 5:
            if page > 1:
                url_args["page"] = page - 1
                previous_href = url_for(url_endpoint, **url_args)

            if page < n_pages:
                url_args["page"] = page + 1
                next_href = url_for(url_endpoint, **url_args)

        return {
            "previous_href": previous_href,
            "next_href": next_href,
            "pages": pages,
        }

    def get_pages(self, page, n_pages, url_endpoint, url_args):
        pages = []
        if n_pages <= 5:
            for i in range(1, n_pages+1):
                url_args["page"] = i
                pages.append(self.get_page_data(
                    page=i,
                    active_page=page,
                    url_endpoint=url_endpoint,
                    url_args=url_args
                ))
        else:
            if page < n_pages / 2:
                if page == 1:
                    for i in range(1, 6):
                        url_args["page"] = i
                        pages.append(self.get_page_data(
                            page=i,
                            active_page=page,
                            url_endpoint=url_endpoint,
                            url_args=url_args
                        ))
                else:
                    for i in range(-1, 4):
                        url_args["page"] = page+i
                        pages.append(self.get_page_data(
                            page=page+i,
                            active_page=page,
                            url_endpoint=url_endpoint,
                            url_args=url_args
                        ))
                pages[3] = self.get_suspension_points()
                pages[4] = self.get_page_data(
                            page=n_pages,
                            active_page=page,
                            url_endpoint=url_endpoint,
                            url_args=url_args
                        )
            else:
                if page == n_pages:
                    for i in range(-4, 1):
                        url_args["page"] = page+i
                        pages.append(self.get_page_data(
                            page=page+i,
                            active_page=page,
                            url_endpoint=url_endpoint,
                            url_args=url_args
                        ))
                else:
                    for i in range(-3, 2):
                        url_args["page"] = page+i
                        pages.append(self.get_page_data(
                            page=page+i,
                            active_page=page,
                            url_endpoint=url_endpoint,
                            url_args=url_args
                        ))
                pages[1] = self.get_suspension_points()
                pages[0] = self.get_page_data(
                            page=1,
                            active_page=page,
                            url_endpoint=url_endpoint,
                            url_args=url_args
                        )
        return pages

    def get_suspension_points(self):
        return {
            "text": "..."
        }

    def get_page_data(self, page, active_page, url_endpoint, url_args):
        url_args["page"] = page
        page_data = {
            "text": page,
            "href": url_for(url_endpoint, **url_args)
        }
        if int(page_data["text"]) == active_page:
            page_data["active"] = True
        return page_data


paginator_data_provider = PaginatorDataProvider()
