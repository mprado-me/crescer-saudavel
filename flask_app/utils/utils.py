#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, math

class Utils():
    @staticmethod
    # dic2 keys overrides dic1 keys
    def new_dic(dic1, dic2):
        result = dict(dic1)
        print json.dumps(result)
        for key, value in dic2.iteritems():
            result[key] = value
        return result

    @staticmethod
    def get_n_pages(n_items, per_page):
        n_pages = int(math.ceil(float(n_items) / per_page))
        n_pages = max(1, n_pages)
        return n_pages

    @staticmethod
    def get_valid_page(page, n_items, per_page):
        n_pages = Utils.get_n_pages(n_items=n_items, per_page=per_page)
        return Utils.get_limited(value=page, min_limit=1, max_limit=n_pages)

    @staticmethod
    def get_limited(value, min_limit, max_limit):
        value = max(min_limit, value)
        value = min(value, max_limit)
        return value

    @staticmethod
    def get_page_range(page, n_items, per_page):
        page = Utils.get_valid_page(page=page, n_items=n_items, per_page=per_page)
        first = (page - 1) * per_page
        last_plus_one = first + per_page
        return (first, last_plus_one)