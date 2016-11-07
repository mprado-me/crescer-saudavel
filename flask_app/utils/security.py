#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from itsdangerous import URLSafeTimedSerializer

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])