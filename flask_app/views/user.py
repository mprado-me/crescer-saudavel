#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, url_for, redirect, abort, session

from flask_app import app, db

from ..data_providers.about_us import AboutUsDataProvider
from ..data_providers.blog import BlogDataProvider
from ..data_providers.blog_post_data_provider import BlogPostDataProvider
from ..data_providers.cart import CartDataProvider
from ..data_providers.checkout import CheckoutDataProvider
from ..data_providers.sent_confirmation_email import SentConfirmationEmailDataProvider
from ..data_providers.create_account import CreateAccountDataProvider
from ..data_providers.get_fail import GetFailDataProvider
from ..data_providers.faq import FaqDataProvider
from ..data_providers.recover_password import RecoverPasswordDataProvider
from ..data_providers.sent_recover_password_email import SentRecoverPasswordEmailDataProvider
from ..data_providers.home import HomeDataProvider
from ..data_providers.login import LoginDataProvider
from ..data_providers.my_account import MyAccountDataProvider
from ..data_providers.order import OrderDataProvider
from ..data_providers.product import ProductDataProvider
from ..data_providers.products import ProductsDataProvider
from ..data_providers.redefine_password import RedefinePasswordData
from flask_app.data_providers.resend_confirmation_email_data_provider import get_resend_confirmation_email_data

from flask_app.utils.mock import is_user_registred

from flask_app.utils.email_manager import send_create_account_confirmation_email, send_redefine_password_email

from flask_app.forms import CreateAccountForm, LoginForm, EmailForm, RedefinePasswordForm

from flask_app.models import User

from flask_app.utils.security import ts

from flask_login import login_user, login_required, logout_user

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

@app.route('/email-de-confirmacao-enviado')
def sent_confirmation_email():
    email = request.args.get("email")
    if not email:
        abort(422)
    data = SentConfirmationEmailDataProvider().get_data(email)
    return render_template("confirmation-email-sending.html", data=data)
    
@app.route('/criar-conta', methods=['GET', 'POST'])
def create_account():
    form = CreateAccountForm()
    if request.method == "GET":
        data = CreateAccountDataProvider().get_data(form)
        return render_template('create-account.html', data=data)
    else:
        invalid_form = not form.validate_on_submit()

        # Checking if the email is already registered
        email_registered = False
        try:
            if db.session.query(User).filter_by(email=form.email.data).first():
                email_registered = True
        except:
            db.session.rollback()
            return create_account_db_error(form)
            
        if invalid_form or email_registered:
            data = CreateAccountDataProvider().get_data(form)
            if email_registered:
                data["form"].email.errors.append('Email já registrado')
            return render_template('create-account.html', data=data)

        user = User(
            email = form.email.data,
            password = form.password.data
        )

        # Adding user in db
        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            return create_account_db_error(form)

        # Sending confirmation email message
        try:
            send_create_account_confirmation_email(user.email)
            return redirect(url_for("sent_confirmation_email", email=request.form["email"]))
        except:
            # TODO: Redirect to remand confirmation email page, the user has already been registered
            msg = {
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao enviar o email de confirmação. Tente novamente.",
            }
            data = CreateAccountDataProvider().get_data(form, msg=msg)
            return render_template('create-account.html', data=data)

def create_account_db_error(form):
    msg = {
        "type": "danger",
        "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
    }
    data = CreateAccountDataProvider().get_data(form, msg=msg)
    return render_template('create-account.html', data=data)

@app.route('/email-confirmado/<token>')
def email_confirmed(token):
    try:
        email = ts.loads(token, salt="email-confirm-key")
    except:
        abort(404)

    try:
        user = User.query.filter_by(email=email).first_or_404()
        user.email_confirmed = True
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
        msg = {
            "type": "danger",
            "content": "Falha! Ocorreu um erro ao acessar o banco de dados.",
        }
        button = {
            "title": "Tentar novamente",
            "href": url_for('email_confirmed', token=token)
        }
        data = GetFailDataProvider().get_data(msg=msg, button=button)
        return render_template('get-fail.html', data=data)

    return redirect(url_for('login', msg_content="Email confirmado com sucesso.", msg_type="success"))

@app.route('/faq')
def faq():
    data = FaqDataProvider().get_data()
    return render_template('faq.html', data=data)

@app.route('/recuperar-senha', methods=["GET", "POST"])
def recover_password():
    form = EmailForm()
    if request.method == "GET":
        data = RecoverPasswordDataProvider().get_data(form=form)
        return render_template('forgot-password.html', data=data)
    elif request.method == "POST":
        invalid_form = not form.validate_on_submit()
        email_registered = None
        email_confirmed = None
        user = None

        try:
            user = db.session.query(User).filter_by(email=form.email.data).first()

            if user:
                email_registered = True
                email_confirmed = user.email_confirmed
            else:
                email_registered = False
        except:
            db.session.rollback()
            msgs = []
            msgs.append({
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
            })
            data = RecoverPasswordDataProvider().get_data(form=form, msgs=msgs)
            return render_template('forgot-password.html', data=data)

        if invalid_form:
            data = RecoverPasswordDataProvider().get_data(form=form)
            return render_template('forgot-password.html', data=data)

        if not email_registered:
            data = RecoverPasswordDataProvider().get_data(form=form)
            data["form"].email.errors.append("Email não registrado")
            return render_template('forgot-password.html', data=data)

        if not email_confirmed:
            data = RecoverPasswordDataProvider().get_data(form=form)
            data["form"].email.errors.append("Email não confirmado. Para reenviar o email de confirmação clique <a href='%s'>aqui</a>." % url_for("resend_confirmation_email") )
            return render_template('forgot-password.html', data=data)

        # Sending redefine password email message
        try:
            send_redefine_password_email(user.email)
            return redirect(url_for("sent_recover_password_email", email=user.email))
        except:
            msgs = []
            msgs.append({
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao enviar o email de redefinição de senha. Tente novamente.",
            })
            data = RecoverPasswordDataProvider().get_data(form=form, msgs=msgs)
            return render_template('forgot-password.html', data=data)

    abort(404)

@app.route('/email-de-recuperacao-de-senha-enviado')
def sent_recover_password_email():
    email = request.args.get("email")
    if not email:
        abort(422)
    data = SentRecoverPasswordEmailDataProvider().get_data(email=email)
    return render_template('sent-recover-password-email.html', data=data)

@app.route('/')
@app.route('/home')
def home():
    data = HomeDataProvider().get_data()
    return render_template('home.html', data=data)

@app.route('/entrar', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "GET":
        msgs = []
        msg_content = request.args.get("msg_content")
        msg_type = request.args.get("msg_type")
        if msg_content and msg_type:
            msgs.append({
                "type": msg_type,
                "content": msg_content,
            })
        finalizando_compra = request.args.get('finalizando_compra')
        if finalizando_compra and finalizando_compra == "sim":
            msgs.append({
                "type": "info",
                "content": "Para finalizar a compra, entre ou cadastre-se.",
            })
        data = LoginDataProvider().get_data(form=form, msgs=msgs)
        return render_template('login.html', data=data)
    else:
        invalid_form = not form.validate_on_submit()
        incorrect_password = None
        email_registered = None
        email_confirmed = None

        try:
            user = db.session.query(User).filter_by(email=form.email.data).first()

            if user:
                email_registered = True
                incorrect_password = not user.is_correct_password(form.password.data)
                email_confirmed = user.email_confirmed

                if not incorrect_password and email_confirmed:
                    user.authenticated = True
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    return redirect(url_for('my_account'))
            else:
                email_registered = False
        except:
            db.session.rollback()
            msgs = []
            msgs.append({
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
            })
            data = LoginDataProvider().get_data(form=form, msgs=msgs)
            return render_template('login.html', data=data)

        if invalid_form:
            data = LoginDataProvider().get_data(form=form)
            return render_template('login.html', data=data)

        if not email_registered:
            data = LoginDataProvider().get_data(form=form)
            data["form"].email.errors.append("Email não registrado")
            return render_template('login.html', data=data)

        if not email_confirmed:
            data = LoginDataProvider().get_data(form=form)
            data["form"].email.errors.append("Email não confirmado. Para reenviar o email de confirmação clique <a href='%s'>aqui</a>." % url_for("resend_confirmation_email") )
            return render_template('login.html', data=data)

        if incorrect_password:
            data = LoginDataProvider().get_data(form=form)
            data["form"].password.errors.append("Senha incorreta")
            return render_template('login.html', data=data)

        abort(404)

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

@app.route('/produto/<int:product_id>')
def product(product_id):
    data = ProductDataProvider().get_data(product_id)
    return render_template('product.html', data=data)

@app.route('/produtos/pagina/<int:page>/ordenacao/<int:sort_method>')
def all_products(page, sort_method):
    data = ProductsDataProvider().get_all_products_data(page=page, sort_method=sort_method)
    return render_template('products.html', data=data)

@app.route('/produtos/categoria/<int:category_id>/pagina/<int:page>/ordenacao/<int:sort_method>')
def products_by_category(category_id, page, sort_method):
    data = ProductsDataProvider().get_products_data_by_category(category_id=category_id, page=page, sort_method=sort_method)
    return render_template('products.html', data=data)

@app.route('/produtos/categoria/<int:category_id>/subcategoria/<int:subcategory_id>/pagina/<int:page>/ordenacao/<int:sort_method>')
def products_by_category_and_subcategory(category_id, subcategory_id, page, sort_method):
    data = ProductsDataProvider().get_products_data_by_category_and_subcategory(category_id=category_id, subcategory_id=subcategory_id, page=page, sort_method=sort_method)
    return render_template('products.html', data=data)

@app.route('/produtos/busca/pagina/<int:page>/ordenacao/<int:sort_method>')
def products_by_search(page, sort_method):
    q = request.args.get('q')
    data = ProductsDataProvider().get_products_data_by_search(page=page, sort_method=sort_method, q=q)
    return render_template('products.html', data=data)

@app.route('/redefinir-senha/<token>', methods=["GET", "POST"])
def redefine_password(token):
    try:
        email = ts.loads(token, salt="recover-key")
    except:
        abort(404)

    form = RedefinePasswordForm()

    if request.method == "GET":
        data = RedefinePasswordData().get_data(form=form, email=email, token=token, msgs=[])
        return render_template('redefine-password.html', data=data)
    elif request.method == "POST":
        invalid_form = not form.validate_on_submit()

        if invalid_form:
            data = RedefinePasswordData().get_data(form=form, email=email, token=token, msgs=[])
            return render_template('redefine-password.html', data=data)

        # Changing user password
        try:
            user = User.query.filter_by(email=email).first_or_404()
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            msgs = []
            msgs.append({
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
            })
            data = RedefinePasswordData().get_data(form=form, email=email, token=token, msgs=msgs)
            return render_template('redefine-password.html', data=data)

        return redirect(url_for('login', msg_type="success", msg_content="Senha redefinida com sucesso."))
    return None
    

@app.route('/reenviar-email-de-confirmacao', methods=['GET', 'POST'])
def resend_confirmation_email():
    form = EmailForm()
    if request.method == 'GET':
        data = get_resend_confirmation_email_data(form)
        return render_template('resend-confirmation-email.html', data=data)
    elif request.method == 'POST':
        invalid_form = not form.validate_on_submit()
        email_registered = None
        email_confirmed = None

        try:
            user = db.session.query(User).filter_by(email=form.email.data).first()

            if user:
                email_registered = True
                email_confirmed = user.email_confirmed
            else:
                email_registered = False
        except:
            db.session.rollback()
            msgs = []
            msgs.append({
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
            })
            data = get_resend_confirmation_email_data(form=form, msgs=msgs)
            return render_template('resend-confirmation-email.html', data=data)

        if invalid_form:
            data = get_resend_confirmation_email_data(form=form)
            return render_template('resend-confirmation-email.html', data=data)

        if not email_registered:
            data = get_resend_confirmation_email_data(form=form)
            data["form"].email.errors.append("Email não registrado. Clique <a href='%s'>aqui</a> para criar uma nova conta." % url_for("create_account"))
            return render_template('resend-confirmation-email.html', data=data)

        if email_confirmed:
            data = get_resend_confirmation_email_data(form=form)
            data["form"].email.errors.append("Email já confirmado. Clique <a href='%s'>aqui</a> para entrar na conta." % url_for("login"))
            return render_template('resend-confirmation-email.html', data=data)

        # Sending confirmation message
        # TODO: Restrict the resend of the same email to one hour using a new table
        try:
            send_create_account_confirmation_email(form.email.data)
            return redirect(url_for("sent_confirmation_email", email=form.email.data))
        except:
            msgs = []
            msgs.append({
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao reenviar o email de confirmação. Tente novamente.",
            })
            data = get_resend_confirmation_email_data(form=form, msgs=msgs)
            return render_template('resend-confirmation-email.html', data=data)
    abort(404)

@app.route('/sair')
def logout():
    logout_user()
    return redirect(url_for('login'))

# print "app.config['MAIL_FROM_EMAIL']: " + app.config["MAIL_FROM_EMAIL"]
# print "app.config['SECRET_KEY']: " + app.config["SECRET_KEY"]