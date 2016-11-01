#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_footer_data():
	return get_sample_data_0()

def get_sample_data_0():
	data = {
		"address": "Rua ..., n 25, SJC - SP",
		"tel": "(11) 1234-5678",
		"email": "email@email.com",
		"social_networks": [
			{
				"title": "Facebook",
				"class": "fb",
				"href": "#",
			},
			{
				"title": "Twitter",
				"class": "tw",
				"href": "#",
			},
			{
				"title": "Google Plus",
				"class": "googleplus",
				"href": "#",
			},
			{
				"title": "Youtube",
				"class": "youtube",
				"href": "#",
			},
		],
		"products": [
			{
				"name": "Frutas",
				"category_id": "1",
			},
			{
				"name": "Sopa creme",
				"category_id": "2",
			},
			{
				"name": "Sopa com pedaços",
				"category_id": "3",
			},
			{
				"name": "Linha Single",
				"category_id": "4",
			},
			{
				"name": "Linha Emporinho",
				"category_id": "5",
			},
		],
		"blog_posts": [
			{
				"title": "Título do post 0",
				"blog_post_id": "0",
			},
			{
				"title": "Título do post 1",
				"blog_post_id": "1",
			},
			{
				"title": "Título do post 2",
				"blog_post_id": "2",
			},
			{
				"title": "Título do post 3",
				"blog_post_id": "3",
			},
			{
				"title": "Título do post 4",
				"blog_post_id": "4",
			},
		],
		"copyright_text": "Copyright © 2016 - Crescer Saudável",
	}
	return data