#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from header_data_provider import get_header_data
from footer_data_provider import get_footer_data

def get_home_data():
	return sample_data_0()

def sample_data_0():
	data = {
		"header_data": get_header_data(),
		"footer_data": get_footer_data(),
		"carousel": [
			{
				"img_src": "static/images/slide-img2.jpg",
				"title": "Título 1",
				"subtitle": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam facilisis, nisi in convallis dignissim."
			},
			{
				"img_src": "static/images/slide-img2.jpg",
				"title": "Título 2",
				"subtitle": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam facilisis, nisi in convallis dignissim."
			},
		],
		"sections": [
			{
				"title": "Novidades",
				"products": [
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
				]
			},
			{
				"title": "Mais vendidos",
				"products": [
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
				]
			},
		],
		"blog_post_0_data": {
			"title": "Lorem ipsum dolor sit amet, consectetur adipiscing",
			"img_src": "static/images/blog-img1.jpg",
			"href": url_for('blog_post', blog_post_id=0),
			"day": "19",
			"month": "Março",
		},
		"blog_post_1_data": {
			"title": "Lorem ipsum dolor sit amet, consectetur adipiscing",
			"img_src": "static/images/blog-img1.jpg",
			"href": url_for('blog_post', blog_post_id=0),
			"day": "06",
			"month": "Março",
		},
	}
	return data

def sample_data_1():
	data = {
		"header_data": get_header_data(),
		"footer_data": get_footer_data(),
		"sections": [
			{
				"title": "Novidades",
				"products": [
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
				]
			},
			{
				"title": "Novidades",
				"products": [
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
				]
			},
			{
				"title": "Mais vendidos",
				"products": [
				]
			},
		],
		"blog_post_0_data": {
			"title": "Lorem ipsum dolor sit amet, consectetur adipiscing",
			"img_src": "static/images/blog-img1.jpg",
			"href": url_for('blog_post', blog_post_id=0),
			"day": "19",
			"month": "Março",
		},
	}
	return data

def sample_data_2():
	data = {
		"header_data": get_header_data(),
		"footer_data": get_footer_data(),
		"carousel": [
			{
				"img_src": "static/images/slide-img2.jpg",
				"title": "Título 1",
				"subtitle": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam facilisis, nisi in convallis dignissim."
			},
		],
		"sections": [
			{
				"title": "Novidades",
				"products": [
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
				]
			},
			{
				"title": "Novidades",
				"products": [
					{
						"title": "Nome do produto",
						"product_id": 0,
						"href": url_for("product", product_id=0),
						"img_src": "/static/images/products/p1.jpg",
						"price": "R$ 0,00",
					},
				]
			},
		],
	}
	return data