#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms.widgets import html_params

def personalized_textarea(field, **kwargs):
    example = kwargs.pop('example', "")
    markdown = kwargs.pop('markdown', False)
    options = dict(kwargs, name=field.name, id=field.name)
    if not field.data:
        field.data = ""
    html = []
    html.append(u'<textarea %s>%s</textarea>' % (html_params(**options), field.data))
    html.append(u'<br>')
    if markdown:
        html.append(u"""<div class="markdown-container"><span class="label label-default markdown">Formato Markdown</span>""")
        html.append(u'Para saber mais sobre Markdown, acesse: <a target="_blank" href="https://support.zendesk.com/hc/pt-br/articles/203691016-Formata%C3%A7%C3%A3o-de-texto-com-Markdown">markdown básico</a> ou <a target="_blank" href="http://aprender19.unb.br/help.php?file=advanced_markdown.html">markdown avançado</a></div>')
        if example:
            html.append(u'<br>')
    if example:
        html.append(u"""<div class="jumbotron example-jumbotron"><b>Exemplo: </b><br>%s</div>""" % example)
    return u''.join(html)