#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app


class DatabaseAccessError(Exception):
    msg = {
        "type": "danger",
        "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
    }

    def __init__(self, message="", exception=None):
        super(DatabaseAccessError, self).__init__(message)
        log_exception(name="DatabaseAccessError", message=message, exception=exception)


class EmailSendingError(Exception):
    msg = {
        "type": "danger",
        "content": "Falha! Ocorreu um erro ao enviar o email. Tente novamente.",
    }

    def __init__(self, message="", exception=None):
        super(EmailSendingError, self).__init__(message)
        log_exception(name="EmailSendingError", message=message, exception=exception)


class InvalidQueryParamError(Exception):
    def __init__(self, message=""):
        super(InvalidQueryParamError, self).__init__(message)
        log_exception(name="InvalidQueryParamError", message=message)


class InvalidParamError(Exception):
    def __init__(self, message=""):
        super(InvalidParamError, self).__init__(message)
        log_exception(name="InvalidParamError", message=message)


class InvalidUrlParamError(Exception):
    def __init__(self, message=""):
        super(InvalidUrlParamError, self).__init__(message)
        log_exception(name="InvalidUrlParamError", message=message)


def log_exception(name, message="", exception=None):
    app.logger.error("-*-*-")
    if message != "":
        app.logger.error(name + " | " + message)
    else:
        app.logger.error(name)
    if exception:
        app.logger.exception(exception)


def log_unrecognized_exception(e):
    app.logger.error("-*-*-")
    app.logger.error("UnrecognizedException")
    app.logger.exception(e)
