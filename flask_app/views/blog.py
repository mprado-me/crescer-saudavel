#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..data_providers.blog import blog_data_provider
from ..data_providers.blog_post_data_provider import blog_post_data_provider

from flask import render_template, request


@app.route('/blog/pagina/<int:page>')
def blog(page):
    data = blog_data_provider.get_data(page=page)
    return render_template('blog/blog.html', data=data)


@app.route('/blog-post/<int:blog_post_id>')
def blog_post(blog_post_id):
    # Getting optional parameters
    blog_page_to_return = request.args.get('blog-page-to-return')

    # Setting default value to optional parameters
    if not blog_page_to_return:
        blog_page_to_return = 1

    data = blog_post_data_provider.get_data(blog_post_id=blog_post_id, blog_page_to_return=blog_page_to_return)
    return render_template('blog/blog-post.html', data=data)
