#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for
from header import HeaderDataProvider
from footer import FooterDataProvider

class HomeDataProvider():

	def get_data(self):
		return self.sample_data_0()

	def get_section(self, section_title):
		return {
			"title": section_title,
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
		}

	def sample_data_0(self):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"footer_data": FooterDataProvider().get_data(),
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
				self.get_section("Ofertas"),
				self.get_section("Novidades"),
				self.get_section("Mais vendidos"),
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

	def sample_data_1(self):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"footer_data": FooterDataProvider().get_data(),
			"sections": [
				self.get_section("Ofertas"),
				self.get_section("Novidades"),
				self.get_section("Mais vendidos"),
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

	def sample_data_2(self):
		data = {
			"header_data": HeaderDataProvider().get_data(),
			"footer_data": FooterDataProvider().get_data(),
			"carousel": [
				{
					"img_src": "static/images/slide-img2.jpg",
					"title": "Título 1",
					"subtitle": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam facilisis, nisi in convallis dignissim."
				},
			],
			"sections": [
				self.get_section("Ofertas"),
				self.get_section("Novidades"),
				self.get_section("Mais vendidos"),
			],
		}
		return data