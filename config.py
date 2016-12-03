#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

DEBUG = False
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'crescer.saudavel.suporte@gmail.com'
MAIL_USE_TLS = False
MAIL_USE_SSL = True

USER_PRODUCTS_PAGINATOR_SIZE = 4
USER_BLOG_PAGINATOR_SIZE = 3

DEFAULT_PAGINATOR_SIZE = 3
DEFAULT_N_ITEMS_PER_PAGE = 5

ADMIN_N_IMAGES_PER_PAGE = 20

ADMIN_N_PRODUCTS_PER_PAGE = 20

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_FILENAME = 'logs/log'
LOGGING_LEVEL = logging.DEBUG

UPLOADED_IMAGES_FOLDER = '/vagrant/flask_app/static/uploads/images'

SQLALCHEMY_TRACK_MODIFICATIONS = False
