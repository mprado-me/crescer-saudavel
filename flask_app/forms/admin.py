#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..utils.validators import AllowedFileFormat, HasFilePart

from flask_wtf import FlaskForm

from wtforms import FileField

none_file_selected_msg = "Nenhum arquivo foi selecionado"
invalid_file_format_msg = "Formato de arquivo inválido"

class UploadImageForm(FlaskForm):
    image = FileField('Image', validators=[
        HasFilePart(input_file_name="file", message=none_file_selected_msg),
        AllowedFileFormat(input_file_name="file", allowed_extensions=["png", "jpg", "jpeg"], message=invalid_file_format_msg)])