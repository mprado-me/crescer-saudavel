#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app import app

from flask_app.data_providers.customer.blog.blog import blog_data_provider
from flask_app.data_providers.customer.blog.blog_post import blog_post_data_provider

from flask_app.utils.decorators import log_route
from flask_app.utils.exceptions import log_unrecognized_exception

from flask import abort, render_template, request


@app.route('/blog/pagina/<int:page>')
@log_route
def blog(page):
    try:
        data = blog_data_provider.get_data(page=page)
        return render_template('customer/blog/blog.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/blog-post/<int:blog_post_id>')
@log_route
def blog_post(blog_post_id):
    try:
        # Getting optional parameters
        blog_page_to_return = request.args.get('blog-page-to-return')

        # Setting default value to optional parameters
        if not blog_page_to_return:
            blog_page_to_return = 1

        data = blog_post_data_provider.get_data(blog_post_id=blog_post_id, blog_page_to_return=blog_page_to_return)
        return render_template('customer/blog/blog-post.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
