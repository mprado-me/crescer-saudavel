#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

DEBUG = False
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'crescer.saudavel.suporte@gmail.com'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
N_PAGES_IN_PRODUCTS_PAGINATOR = 4
N_PAGES_IN_BLOG_PAGINATOR = 3

DEFAULT_N_PAGES_IN_PAGINATOR = 3
DEFAULT_N_ITEMS_BY_PAGE = 5

N_PAGES_IN_ADMIN_IMAGES = 5
N_ITEMS_BY_PAGE_IN_ADMIN_IMAGES = 20

ADMIN_N_PAGES_IN_PRODUCTS_PAGINATOR = 5
ADMIN_N_PRODUCTS_BY_PAGE = 10

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_FILENAME = 'logs/log'
LOGGING_LEVEL = logging.DEBUG

UPLOADED_IMAGES_FOLDER = '/vagrant/flask_app/static/uploads/images'