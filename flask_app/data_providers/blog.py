#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from header import HeaderDataProvider
from footer import FooterDataProvider
from paginator import PaginatorDataProvider

from flask import url_for

class BlogDataProvider():

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
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": self.get_page_heading_data(),
			"footer_data": FooterDataProvider().get_data(),
			"paginator_data": PaginatorDataProvider().get_data(
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
			"header_data": HeaderDataProvider().get_data(),
			"page_heading_data": {
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
			},
			"footer_data": FooterDataProvider().get_data(),
			"paginator_data": PaginatorDataProvider().get_data(
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