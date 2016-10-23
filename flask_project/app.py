import sys

from flask import Flask, jsonify, render_template, request, url_for

from data_providers.about_us_data_provider import get_about_us_data
from data_providers.blog_data_provider import get_blog_data
from data_providers.blog_post_data_provider import get_blog_post_data
from data_providers.cart_data_provider import get_cart_data
from data_providers.checkout_data_provider import get_checkout_data
from data_providers.create_account_data_provider import get_create_account_data
from data_providers.faq_data_provider import get_faq_data
from data_providers.forgot_password_data_provider import get_forgot_password_data
from data_providers.forgot_password_email_sending_data_provider import get_forgot_password_email_sending_data
from data_providers.home_data_provider import get_home_data
from data_providers.login_data_provider import get_login_data
from data_providers.my_account_data_provider import get_my_account_data
from data_providers.new_password_data_provider import get_new_password_data
from data_providers.order_data_provider import get_order_data
from data_providers.product_data_provider import get_product_data
from data_providers.products_data_provider import get_all_products_data, get_products_data_by_category, get_products_data_by_category_and_subcategory, get_products_data_by_search

from enums.sort_method import SortMethod

app = Flask(__name__)

@app.route('/sobre-nos')
def about_us():
    data = get_about_us_data()
    return render_template('about-us.html', data=data)

@app.route('/blog-post/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_page_to_return = request.args.get('blog-page-to-return')
    if not blog_page_to_return:
        blog_page_to_return = 1
    data = get_blog_post_data(blog_post_id=blog_post_id, blog_page_to_return=blog_page_to_return)
    return render_template('blog-post.html', data=data)

@app.route('/blog/<int:page>')
def blog(page):
    data = get_blog_data(page=page)
    return render_template('blog.html')

@app.route('/carrinho')
def cart():
    data = get_cart_data()
    return render_template('cart.html', cart_table_editable=True, data=data)

@app.route('/finalizacao-de-compra/<int:step>')
def checkout(step):
    data = get_checkout_data()
    data = {
        "in_edit_info_mode": True,
    }
    return render_template('checkout.html', cart_table_editable=False, step=step, data=data)

@app.route('/criar-conta')
def create_account():
    data = get_create_account_data()
    return render_template('create-account.html', data=data)

@app.route('/faq')
def faq():
    data = get_faq_data()
    return render_template('faq.html', data=data)

@app.route('/recuperacao-de-senha')
def forgot_password():
    data = get_forgot_password_data()
    return render_template('forgot-password.html', data=data)

@app.route('/envio-do-email-de-recuperacao-de-senha')
def forgot_password_email_sending():
    data = get_forgot_password_email_sending_data()
    return render_template('forgot-password-email-sending.html', data=data)

@app.route('/')
@app.route('/home')
def home():
    data = get_home_data()
    return render_template('home.html', data=data)

@app.route('/entrar')
def login():
    data = get_login_data()
    return render_template('login.html', data=data)

@app.route('/minha-conta')
def my_account():
    data = get_my_account_data()
    data = {
        "in_edit_info_mode": False,
    }
    return render_template('my-account.html', data=data)

@app.route('/nova-senha')
def new_password():
    data = get_new_password_data()
    return render_template('new-password.html', data=data)

@app.route('/pedido/<int:order_id>')
def order(order_id):
    data = get_order_data(order_id)
    return render_template('order.html', data=data)

@app.route('/produto/<int:product_id>')
def product(product_id):
    data = get_product_data(product_id)
    return render_template('product.html', data=data)

@app.route('/produtos/pagina/<int:page>/ordenacao/<int:sort_method>')
def all_products(page, sort_method):
    data = get_all_products_data(page=page, sort_method=sort_method)
    return render_template('products.html', data=data)

@app.route('/produtos/categoria/<int:category_id>/pagina/<int:page>/ordenacao/<int:sort_method>')
def products_by_category(category_id, page, sort_method):
    data = get_products_data_by_category(category_id=category_id, page=page, sort_method=sort_method)
    return render_template('products.html', data=data)

@app.route('/produtos/categoria/<int:category_id>/subcategoria/<int:subcategory_id>/pagina/<int:page>/ordenacao/<int:sort_method>')
def products_by_category_and_subcategory(category_id, subcategory_id, page, sort_method):
    data = get_products_data_by_category_and_subcategory(category_id=category_id, subcategory_id=subcategory_id, page=page, sort_method=sort_method)
    return render_template('products.html', data=data)

@app.route('/produtos/busca/pagina/<int:page>/ordenacao/<int:sort_method>')
def products_by_search(page, sort_method):
    q = request.args.get('q')
    data = get_products_data_by_search(page=page, sort_method=sort_method, q=q)
    return render_template('products.html', data=data)

if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == 'local':
		app.debug = True
		app.run(host='0.0.0.0', port=5000)
	else:
		app.run()