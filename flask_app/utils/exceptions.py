#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

import traceback

class DatabaseAccessError(Exception):
    def __init__(self, message=""):
        super(DatabaseAccessError, self).__init__(message)
        app.logger.warning("-*-*-")
        if message != "":
            app.logger.warning("DatabaseAccessError | " + message)
        else:
            app.logger.warning("DatabaseAccessError")
        traceback_as_string = "".join(traceback.format_stack())
        app.logger.warning("\n"+traceback_as_string)
