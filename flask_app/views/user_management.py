#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, url_for, redirect, abort

from flask_login import login_user, logout_user

from .. import app, db

from ..forms import CreateAccountForm, LoginForm, EmailForm, RedefinePasswordForm
from ..models import User
from ..utils.email_manager import send_create_account_confirmation_email, send_redefine_password_email
from ..utils.security import ts

from ..data_providers.sent_confirmation_email import SentConfirmationEmailDataProvider
from ..data_providers.create_account import CreateAccountDataProvider
from ..data_providers.get_fail import GetFailDataProvider
from ..data_providers.recover_password import RecoverPasswordDataProvider
from ..data_providers.sent_recover_password_email import SentRecoverPasswordEmailDataProvider
from ..data_providers.login import LoginDataProvider
from ..data_providers.redefine_password import RedefinePasswordData
from ..data_providers.resend_confirmation_email import ResendConfirmationEmailDataProvider

@app.route('/email-de-confirmacao-enviado')
def sent_confirmation_email():
    email = request.args.get("email")
    if not email:
        abort(422)
    data = SentConfirmationEmailDataProvider().get_data(email)
    return render_template("user_management/sent-confirmation-email.html", data=data)


@app.route('/criar-conta', methods=['GET', 'POST'])
def create_account():
    form = CreateAccountForm()
    if request.method == "GET":
        data = CreateAccountDataProvider().get_data(form)
        return render_template('user_management/create-account.html', data=data)
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
            return render_template('user_management/create-account.html', data=data)

        user = User(
            email=form.email.data,
            password=form.password.data
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
            return render_template('user_management/create-account.html', data=data)


def create_account_db_error(form):
    msg = {
        "type": "danger",
        "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
    }
    data = CreateAccountDataProvider().get_data(form, msg=msg)
    return render_template('user_management/create-account.html', data=data)


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
        return render_template('shared/get-fail.html', data=data)

    return redirect(url_for('login', msg_content="Email confirmado com sucesso.", msg_type="success"))

@app.route('/recuperar-senha', methods=["GET", "POST"])
def recover_password():
    form = EmailForm()
    if request.method == "GET":
        data = RecoverPasswordDataProvider().get_data(form=form)
        return render_template('user_management/recover-password.html', data=data)
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
            return render_template('user_management/recover-password.html', data=data)

        if invalid_form:
            data = RecoverPasswordDataProvider().get_data(form=form)
            return render_template('user_management/recover-password.html', data=data)

        if not email_registered:
            data = RecoverPasswordDataProvider().get_data(form=form)
            data["form"].email.errors.append("Email não registrado")
            return render_template('user_management/recover-password.html', data=data)

        if not email_confirmed:
            data = RecoverPasswordDataProvider().get_data(form=form)
            data["form"].email.errors.append("Email não confirmado. Para reenviar o email de confirmação clique <a href='%s'>aqui</a>." % url_for("resend_confirmation_email") )
            return render_template('user_management/recover-password.html', data=data)

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
            return render_template('user_management/recover-password.html', data=data)

    abort(404)

@app.route('/email-de-recuperacao-de-senha-enviado')
def sent_recover_password_email():
    email = request.args.get("email")
    if not email:
        abort(422)
    data = SentRecoverPasswordEmailDataProvider().get_data(email=email)
    return render_template('user_management/sent-recover-password-email.html', data=data)

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
        return render_template('user_management/login.html', data=data)
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
            return render_template('user_management/login.html', data=data)

        if invalid_form:
            data = LoginDataProvider().get_data(form=form)
            return render_template('user_management/login.html', data=data)

        if not email_registered:
            data = LoginDataProvider().get_data(form=form)
            data["form"].email.errors.append("Email não registrado")
            return render_template('user_management/login.html', data=data)

        if not email_confirmed:
            data = LoginDataProvider().get_data(form=form)
            data["form"].email.errors.append("Email não confirmado. Para reenviar o email de confirmação clique <a href='%s'>aqui</a>." % url_for("resend_confirmation_email") )
            return render_template('user_management/login.html', data=data)

        if incorrect_password:
            data = LoginDataProvider().get_data(form=form)
            data["form"].password.errors.append("Senha incorreta")
            return render_template('user_management/login.html', data=data)

        abort(404)


@app.route('/redefinir-senha/<token>', methods=["GET", "POST"])
def redefine_password(token):
    try:
        email = ts.loads(token, salt="recover-key")
    except:
        abort(404)

    form = RedefinePasswordForm()

    if request.method == "GET":
        data = RedefinePasswordData().get_data(form=form, email=email, token=token, msgs=[])
        return render_template('user_management/redefine-password.html', data=data)
    elif request.method == "POST":
        invalid_form = not form.validate_on_submit()

        if invalid_form:
            data = RedefinePasswordData().get_data(form=form, email=email, token=token, msgs=[])
            return render_template('user_management/redefine-password.html', data=data)

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
            return render_template('user_management/redefine-password.html', data=data)

        return redirect(url_for('login', msg_type="success", msg_content="Senha redefinida com sucesso."))
    return None


@app.route('/reenviar-email-de-confirmacao', methods=['GET', 'POST'])
def resend_confirmation_email():
    form = EmailForm()
    if request.method == 'GET':
        data = ResendConfirmationEmailDataProvider().get_data(form)
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
            data = ResendConfirmationEmailDataProvider().get_data(form=form, msgs=msgs)
            return render_template('resend-confirmation-email.html', data=data)

        if invalid_form:
            data = ResendConfirmationEmailDataProvider().get_data(form=form)
            return render_template('resend-confirmation-email.html', data=data)

        if not email_registered:
            data = ResendConfirmationEmailDataProvider().get_data(form=form)
            data["form"].email.errors.append(
                "Email não registrado. Clique <a href='%s'>aqui</a> para criar uma nova conta." % url_for(
                    "create_account"))
            return render_template('resend-confirmation-email.html', data=data)

        if email_confirmed:
            data = ResendConfirmationEmailDataProvider().get_data(form=form)
            data["form"].email.errors.append(
                "Email já confirmado. Clique <a href='%s'>aqui</a> para entrar na conta." % url_for("login"))
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
            data = ResendConfirmationEmailDataProvider().get_data(form=form, msgs=msgs)
            return render_template('resend-confirmation-email.html', data=data)
    abort(404)


@app.route('/sair')
def logout():
    logout_user()
    return redirect(url_for('login'))