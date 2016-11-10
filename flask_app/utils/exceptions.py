#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

import traceback

class DatabaseAccessError(Exception):
    msg = {
        "type": "danger",
        "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
    }

    def __init__(self, message=""):
        super(DatabaseAccessError, self).__init__(message)
        app.logger.warning("-*-*-")
        if message != "":
            app.logger.warning("DatabaseAccessError | " + message)
        else:
            app.logger.warning("DatabaseAccessError")
        traceback_as_string = "".join(traceback.format_stack())
        app.logger.warning("\n"+traceback_as_string)

class EmailSendingError(Exception):
    msg = {
        "type": "danger",
        "content": "Falha! Ocorreu um erro ao enviar o email. Tente novamente.",
    }

    def __init__(self, message=""):
        super(EmailSendingError, self).__init__(message)
        app.logger.warning("-*-*-")
        if message != "":
            app.logger.warning("EmailSendingError | " + message)
        else:
            app.logger.warning("EmailSendingError")
        traceback_as_string = "".join(traceback.format_stack())
        app.logger.warning("\n"+traceback_as_string)
