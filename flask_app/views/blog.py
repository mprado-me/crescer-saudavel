#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app

from ..data_providers.blog import BlogDataProvider
from ..data_providers.blog_post_data_provider import BlogPostDataProvider

from flask import render_template, request


@app.route('/blog-post/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_page_to_return = request.args.get('blog-page-to-return')
    if not blog_page_to_return:
        blog_page_to_return = 1
    data = BlogPostDataProvider().get_data(blog_post_id=blog_post_id, blog_page_to_return=blog_page_to_return)
    return render_template('blog/blog-post.html', data=data)


@app.route('/blog/pagina/<int:page>')
def blog(page):
    data = BlogDataProvider().get_data(page=page)
    return render_template('blog/blog.html', data=data)
