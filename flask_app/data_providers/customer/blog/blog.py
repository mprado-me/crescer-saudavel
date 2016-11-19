#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import app

from flask_app.data_providers.customer.shared.footer import footer_data_provider
from flask_app.data_providers.customer.shared.header import header_data_provider
from flask_app.data_providers.customer.shared.paginator import paginator_data_provider

from flask import url_for


class BlogDataProvider:
    def __init__(self):
        pass

    def get_data(self, page=1):
        return self.sample_data_0(page=page)

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": url_for("home"),
                },
                {
                    "name": "Blog",
                },
            ],
            "title": "Blog",
        }

    def sample_data_0(self, page):
        data = {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "footer_data": footer_data_provider.get_data(),
            "paginator_data": paginator_data_provider.get_data(
                current_page=page,
                n_pages=app.config["N_PAGES_IN_BLOG_PAGINATOR"],
                total_n_pages=7,
                url_endpoint="blog",
            ),
            # posts list contains only the the posts of this page
            "posts": [
                {
                    "id": 1,
                    "title": "Lorem ipsum dolor sit amet",
                    "date": "15/10/2016",
                    "thumbnail_href": url_for("static", filename="images/blog-img3.jpg"),
                    "summary": """
                        <p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
                        <p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
                    """,
                },
                {
                    "id": 1,
                    "title": "Lorem ipsum dolor sit amet",
                    "date": "15/10/2016",
                    "thumbnail_href": url_for("static", filename="images/blog-img3.jpg"),
                    "summary": """
                        <p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
                        <p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
                    """,
                },
                {
                    "id": 1,
                    "title": "Lorem ipsum dolor sit amet",
                    "date": "15/10/2016",
                    "thumbnail_href": url_for("static", filename="images/blog-img3.jpg"),
                    "summary": """
                        <p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
                        <p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
                    """,
                },
            ],
        }
        return data

    def sample_data_1(self, page):
        data = {
            "header_data": header_data_provider.get_data(),
            "page_heading_data": self.get_page_heading_data(),
            "footer_data": footer_data_provider.get_data(),
            "paginator_data": paginator_data_provider.get_data(
                current_page=page,
                n_pages=app.config["N_PAGES_IN_BLOG_PAGINATOR"],
                total_n_pages=7,
                url_endpoint="blog",
            ),
            # posts list contains only the the posts of this page
            "posts": [

            ],
        }
        return data

blog_data_provider = BlogDataProvider()
