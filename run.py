#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import app

if app.config["DEBUG"]:
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
else:
	app.debug = False
	app.run()