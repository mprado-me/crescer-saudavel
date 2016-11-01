from flask import render_template, request, url_for, redirect

from flask_app import app

from flask_app.data_providers.about_us_data_provider import get_about_us_data
from flask_app.data_providers.blog_data_provider import get_blog_data
from flask_app.data_providers.blog_post_data_provider import get_blog_post_data
from flask_app.data_providers.cart_data_provider import get_cart_data
from flask_app.data_providers.checkout_data_provider import get_checkout_data
from flask_app.data_providers.confirmation_email_sending_data_provider import get_confirmation_email_sending_data
from flask_app.data_providers.create_account_data_provider import get_create_account_data
from flask_app.data_providers.faq_data_provider import get_faq_data
from flask_app.data_providers.forgot_password_data_provider import get_forgot_password_data
from flask_app.data_providers.forgot_password_email_sending_data_provider import get_forgot_password_email_sending_data
from flask_app.data_providers.home_data_provider import get_home_data
from flask_app.data_providers.login_data_provider import get_login_data
from flask_app.data_providers.my_account_data_provider import get_my_account_data
from flask_app.data_providers.new_password_data_provider import get_new_password_data
from flask_app.data_providers.order_data_provider import get_order_data
from flask_app.data_providers.product_data_provider import get_product_data
from flask_app.data_providers.products_data_provider import get_all_products_data, get_products_data_by_category, get_products_data_by_category_and_subcategory, get_products_data_by_search

from flask_app.utils.mock import is_user_registred

from flask_app.forms import CreateAccountForm

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

@app.route('/blog/pagina/<int:page>')
def blog(page):
    data = get_blog_data(page=page)
    return render_template('blog.html', data=data)

@app.route('/carrinho')
def cart():
    data = get_cart_data()
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
        data = get_checkout_data(step, in_edit_info_mode)
        return render_template('checkout.html', data=data)
    else:
        return redirect(url_for('login', finalizando_compra="sim"))

@app.route('/confirmacao-do-email')
def confirmation_email_sending():
    email = request.args.get("email")
    if not email:
        abort(422)
    data = get_confirmation_email_sending_data(email)
    return render_template("confirmation-email-sending.html", data=data)
    
@app.route('/criar-conta', methods=['GET', 'POST'])
def create_account():
    form = CreateAccountForm()
    if request.method == "GET":
        data = get_create_account_data(form)
        return render_template('create-account.html', data=data)
    else:
        if form.validate_on_submit():
            return redirect(url_for("confirmation_email_sending", email=request.form["email"]))
        data = get_create_account_data(form)
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
    if is_user_registred():
        return redirect(url_for('my_account'))
    else:
        finalizando_compra = request.args.get('finalizando_compra')
        if finalizando_compra and finalizando_compra == "sim":
            finalizando_compra = True
        else:
            finalizando_compra = False
        data = get_login_data(finalizando_compra)
        return render_template('login.html', data=data)

@app.route('/minha-conta', methods=['GET', 'POST'])
def my_account():
    if request.method == 'GET':
        editable = request.args.get("editar")
        if editable and editable == "sim":
            editable = True
        else:
            editable = False
        data = get_my_account_data(editable)
        return render_template('my-account.html', data=data)
    elif request.method == 'POST':
        print request.form
        # TODO: Deal with post
        return redirect(url_for('my_account'))
    return None

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

@app.route('/teste')
def test():
    return render_template('test.html')

# print "app.config['MAIL_FROM_EMAIL']: " + app.config["MAIL_FROM_EMAIL"]
# print "app.config['SECRET_KEY']: " + app.config["SECRET_KEY"]