#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

DEBUG = True

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'crescer.saudavel.suporte@gmail.com'
MAIL_USE_TLS = False
MAIL_USE_SSL = True

DEFAULT_N_ITEMS_PER_PAGE = 5
ADMIN_N_IMAGES_PER_PAGE = 20
ADMIN_N_PRODUCTS_PER_PAGE = 20
ADMIN_N_SUBCATEGORIES_PER_PAGE = 20
ADMIN_N_CATEGORIES_PER_PAGE = 20

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_FILENAME = 'logs/log'
LOGGING_LEVEL = logging.DEBUG

UPLOADED_IMAGES_FOLDER = '/vagrant/flask_app/static/uploads/images'

SQLALCHEMY_TRACK_MODIFICATIONS = False
