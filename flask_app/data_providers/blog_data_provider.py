#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import url_for
from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_blog_data(page=1):
	return sample_data_0()

def sample_data_0():
	n_pages_in_paginator = 4
	data = {
		"header_data": get_header_data(),
		"page_heading_data": {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Blog",
				},
			],
			"title": "Blog",
		},
		"footer_data": get_footer_data(),
		"paginator_data": {
			"previous_href": url_for("blog", page=5),
			"next_href": url_for("blog", page=11),
			"pages": [
				{
					"number": 6,
					"href": url_for("blog", page=6),
				},
				{
					"number": 7,
					"href": url_for("blog", page=7),
					"active": True,
				},
				{
					"number": 8,
					"href": url_for("blog", page=8),
				},
				{
					"number": 9,
					"href": url_for("blog", page=9),
				},
				{
					"number": 10,
					"href": url_for("blog", page=10),
				},
			],
		},
		# posts list contains only the the posts of this page
		"posts": [
			{
				"id": 1,
				"title": "Lorem ipsum dolor sit amet",
				"date": "15/10/2016",
				"thumbnail_href": "/static/images/blog-img3.jpg",
				"summary": """
					<p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
					<p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
				""",
			},
			{
				"id": 1,
				"title": "Lorem ipsum dolor sit amet",
				"date": "15/10/2016",
				"thumbnail_href": "/static/images/blog-img3.jpg",
				"summary": """
					<p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
					<p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
				""",
			},
			{
				"id": 1,
				"title": "Lorem ipsum dolor sit amet",
				"date": "15/10/2016",
				"thumbnail_href": "/static/images/blog-img3.jpg",
				"summary": """
					<p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
					<p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
				""",
			},
		],
	}
	return data

def sample_data_1():
	n_pages_in_paginator = 4
	data = {
		"header_data": get_header_data(),
		"page_heading_data": {
			"path": [
				{
					"name": "Home",
					"href": "/",
				},
				{
					"name": "Blog",
				},
			],
			"title": "Blog",
		},
		"footer_data": get_footer_data(),
		"paginator_data": {
			"n_total_pages": 10,
			"current_page": 1,
			"n_pages_in_paginator": n_pages_in_paginator
		},
		# posts list contains only the the posts of this page
		"posts": [

		],
	}
	return data