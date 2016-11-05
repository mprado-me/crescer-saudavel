#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, url_for, redirect, abort, session

from flask_app import app, db

from ..data_providers.about_us import AboutUsDataProvider
from ..data_providers.blog import BlogDataProvider
from ..data_providers.blog_post_data_provider import BlogPostDataProvider
from ..data_providers.cart import CartDataProvider
from ..data_providers.checkout import CheckoutDataProvider
from ..data_providers.faq import FaqDataProvider
from ..data_providers.home import HomeDataProvider
from ..data_providers.my_account import MyAccountDataProvider
from ..data_providers.order import OrderDataProvider

from flask_app.utils.mock import is_user_registred

from flask_login import login_required

@app.route('/sobre-nos')
def about_us():
    data = AboutUsDataProvider().get_data()
    return render_template('about-us.html', data=data)

@app.route('/blog-post/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_page_to_return = request.args.get('blog-page-to-return')
    if not blog_page_to_return:
        blog_page_to_return = 1
    data = BlogPostDataProvider().get_data(blog_post_id=blog_post_id, blog_page_to_return=blog_page_to_return)
    return render_template('blog-post.html', data=data)

@app.route('/blog/pagina/<int:page>')
def blog(page):
    data = BlogDataProvider().get_data(page=page)
    return render_template('blog.html', data=data)

@app.route('/carrinho')
def cart():
    data = CartDataProvider().get_data()
    return render_template('cart.html', cart_table_editable=True, data=data)

@app.route('/adicionar-ao-carrinho/produto/<int:product_id>/quantidade/<int:quantity>', methods=['POST'])
def cart_add_product(product_id, quantity):
    return redirect(url_for('cart'))

@app.route('/remover-do-carrinho/produto/<int:product_id>/quantidade/<int:quantity>', methods=['POST'])
def cart_remove_product(product_id, quantity):
    return redirect(url_for('cart'))

@app.route('/deletar-do-carrinho/produto/<int:product_id>', methods=['POST'])
def cart_delete_product(product_id):
    return redirect(url_for('cart'))

@app.route('/deletar-tudo-do-carrinho', methods=['POST'])
def cart_delete_all_products():
    return redirect(url_for('cart'))

@app.route('/finalizacao-de-compra/passo/<int:step>')
def checkout(step):
    in_edit_info_mode = request.args.get("editar")
    if in_edit_info_mode and in_edit_info_mode == "sim":
        in_edit_info_mode = True
    else:
        in_edit_info_mode = False
    if is_user_registred():
        data = CheckoutDataProvider().get_data(step, in_edit_info_mode)
        return render_template('checkout.html', data=data)
    else:
        return redirect(url_for('login', finalizando_compra="sim"))

@app.route('/faq')
def faq():
    data = FaqDataProvider().get_data()
    return render_template('faq.html', data=data)

@app.route('/')
@app.route('/home')
def home():
    data = HomeDataProvider().get_data()
    return render_template('home.html', data=data)

@app.route('/minha-conta', methods=['GET', 'POST'])
@login_required
def my_account():
    if request.method == 'GET':
        editable = request.args.get("editar")
        if editable and editable == "sim":
            editable = True
        else:
            editable = False
        data = MyAccountDataProvider().get_data(editable)
        return render_template('my-account.html', data=data)
    elif request.method == 'POST':
        # TODO: Deal with post
        return redirect(url_for('my_account'))
    abort(404)

@app.route('/pedido/<int:order_id>')
def order(order_id):
    data = OrderDataProvider().get_data(order_id)
    return render_template('order.html', data=data)