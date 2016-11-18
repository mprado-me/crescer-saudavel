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

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_FILENAME = 'logs/log'
LOGGING_LEVEL = logging.DEBUG

MAX_CONTENT_LENGTH = 16 * 1024 * 1024
UPLOAD_FOLDER = '/uploads'