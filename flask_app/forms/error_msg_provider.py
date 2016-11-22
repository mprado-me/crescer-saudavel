#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import url_for


class ErrorMsgProvider:
    def __init__(self):
        pass

    def category_too_long(self):
        return "O nome de uma categoria deve ter no máximo 64 caracteres"

    def subcategory_too_long(self):
        return "O nome de uma subcategoria deve ter no máximo 64 caracteres"

    def data_required(self):
        return "Campo obrigatório"

    def email_invalid_format(self):
        return "Formato de email inválido"

    def email_already_registered(self):
        return "Email já cadastrado"

    def email_not_registered(self):
        return "Email não cadastrado. Para criar uma nova conta com este email clique <a href='%s'>aqui</a>." % url_for("create_account")

    def incorrect_password(self):
        return "Senha incorreta"

    def password_length(self):
        return "A senha deve possuir entre 6 e 32 caracteres"

    def password_mismatch(self):
        return "As senhas digitadas não são iguais"

    def unconfirmed_email(self):
        return "Email não confirmado. Para reenviar o email de confirmação clique <a href='%s'>aqui</a>." % url_for("resend_confirmation_email")

    def confirmed_email(self):
        return "Email já confirmado"

    def none_file_selected_msg(self):
        return "Nenhum arquivo foi selecionado"

    def invalid_file_format_msg(self, allowed_extensions):
        allowed_extensions_as_string = ""
        n_allowed_extensions = len(allowed_extensions)

        for i, format in enumerate(allowed_extensions):
            if i == 0:
                allowed_extensions_as_string = format
            elif i == n_allowed_extensions-1:
                allowed_extensions_as_string = allowed_extensions_as_string + " e " + format
            else:
                allowed_extensions_as_string = allowed_extensions_as_string + ", " + format
        return "Formato de arquivo inválido. Os formatos aceitos são: " + allowed_extensions_as_string

error_msg_provider = ErrorMsgProvider()
