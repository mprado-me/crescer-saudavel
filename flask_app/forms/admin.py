#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .error_msg_provider import error_msg_provider

from ..utils.form_field_validators import AllowedFileFormat, HasFilePart

from flask_wtf import FlaskForm

from wtforms import FileField


class UploadImageForm(FlaskForm):
    allowed_extensions = ["png", "jpg", "jpeg"]
    image = FileField('Image', validators=[
        HasFilePart(input_file_name="file", message=error_msg_provider.none_file_selected_msg(), stop=True),
        AllowedFileFormat(
            input_file_name="file",
            allowed_extensions=allowed_extensions,
            message=error_msg_provider.invalid_file_format_msg(allowed_extensions=allowed_extensions)
        )]
    )
