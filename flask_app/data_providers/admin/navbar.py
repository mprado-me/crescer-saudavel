#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for

class NavbarDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return self.sample_data_0()

    def sample_data_0(self):
        data = {
            "menu_items": [
                {
                    "name": "A",
                    "submenu-items": [
                        {
                            "name": "B",
                            "href": url_for("home"),
                        },
                        {
                            "name": "C",
                            "href": url_for("home"),
                        },
                    ],
                },
                {
                    "name": "D",
                    "href": url_for("home"),
                },
                {
                    "name": "E",
                    "href": url_for("home"),
                },
                {
                    "name": "F",
                    "href": url_for("home"),
                    "submenu-items": [
                        {
                            "name": "G",
                            "href": url_for("home"),
                        },
                        {
                            "name": "H",
                            "href": url_for("home"),
                        },
                    ],
                },
            ]
        }
        return data

navbar_data_provider = NavbarDataProvider()
