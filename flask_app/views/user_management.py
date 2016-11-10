#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app, db

from ..data_providers.sent_confirmation_email import sent_confirmation_email_data_provider
from ..data_providers.create_account import create_account_data_provider
from ..data_providers.failed_to_get import failed_to_get_data_provider
from ..data_providers.recover_password import recover_password_data_provider
from ..data_providers.sent_recover_password_email import sent_recover_password_email_data_provider
from ..data_providers.login import login_data_provider
from ..data_providers.redefine_password import redefine_password_data_provider
from ..data_providers.resend_confirmation_email import resend_confirmation_email_data_provider

from ..forms import CreateAccountForm, LoginForm, EmailForm, RedefinePasswordForm

from ..models.user import User

from ..utils.db_manager import db_manager
from ..utils.decorators import log_route
from ..utils.email_manager import send_create_account_confirmation_email, send_redefine_password_email
from ..utils.exceptions import DatabaseAccessError, EmailSendingError, log_exception
from ..utils.security import ts

from flask import abort, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from itsdangerous import BadSignature

@app.route('/email-de-confirmacao-enviado/<string:email>')
@log_route
def sent_confirmation_email(email):
    data = sent_confirmation_email_data_provider.get_data(email)
    return render_template("user_management/sent-confirmation-email.html", data=data)


@app.route('/criar-conta', methods=['GET', 'POST'])
@log_route
def create_account():
    form = CreateAccountForm()

    if request.method == "GET":
        data = create_account_data_provider.get_data(form)
        return render_template('user_management/create-account.html', data=data)

    elif request.method == "POST":
        try:
            if not form.validate_on_submit():
                data = create_account_data_provider.get_data(form)
                return render_template('user_management/create-account.html', data=data)

            user = User(
                email=form.email.data,
                password=form.password.data
            )
            db_manager.add_user(user)

            send_create_account_confirmation_email(form.email.data)

            db_manager.commit()
            return redirect(url_for("sent_confirmation_email", email=request.form["email"]))
        except DatabaseAccessError:
            db_manager.rollback()
            data = create_account_data_provider.get_data_when_database_access_error(form=form)
            return render_template('user_management/create-account.html', data=data)
        except EmailSendingError:
            data = create_account_data_provider.get_data_when_email_sending_error(form=form)
            return render_template('user_management/create-account.html', data=data)


@app.route('/email-confirmado/<token>')
@log_route
def email_confirmed(token):
    try:
        email = ts.loads(token, salt="email-confirm-key")
        user = db_manager.get_user(email=email)
        if not user:
            abort(404)
        user.email_confirmed = True
        db_manager.add_user(user)
        db_manager.commit()
        return redirect(url_for('login', msg_content="Email confirmado com sucesso.", msg_type="success"))
    except BadSignature:
        log_exception(name="BadSignature")
        abort(404)
    except DatabaseAccessError:
        db_manager.rollback()
        href = url_for('email_confirmed', token=token)
        data = failed_to_get_data_provider.get_data_when_database_access_error(href=href)
        return render_template('shared/failed-to-get.html', data=data)


@app.route('/recuperar-senha', methods=["GET", "POST"])
@log_route
def recover_password():
    form = EmailForm()
    if request.method == "GET":
        data = recover_password_data_provider.get_data(form=form)
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
            msgs = [{
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
            }]
            data = recover_password_data_provider.get_data(form=form, msgs=msgs)
            return render_template('user_management/recover-password.html', data=data)

        if invalid_form:
            data = recover_password_data_provider.get_data(form=form)
            return render_template('user_management/recover-password.html', data=data)

        if not email_registered:
            data = recover_password_data_provider.get_data(form=form)
            data["form"].email.errors.append("Email não registrado")
            return render_template('user_management/recover-password.html', data=data)

        if not email_confirmed:
            data = recover_password_data_provider.get_data(form=form)
            data["form"].email.errors.append(
                "Email não confirmado. Para reenviar o email de confirmação clique <a href='%s'>aqui</a>." % url_for(
                    "resend_confirmation_email"))
            return render_template('user_management/recover-password.html', data=data)

        # Sending redefine password email message
        try:
            send_redefine_password_email(user.email)
            return redirect(url_for("sent_recover_password_email", email=user.email))
        except:
            msgs = [{
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao enviar o email de redefinição de senha. Tente novamente.",
            }]
            data = recover_password_data_provider.get_data(form=form, msgs=msgs)
            return render_template('user_management/recover-password.html', data=data)

    abort(404)


@app.route('/email-de-recuperacao-de-senha-enviado')
@log_route
def sent_recover_password_email():
    email = request.args.get("email")
    if not email:
        abort(422)
    data = sent_recover_password_email_data_provider.get_data(email=email)
    return render_template('user_management/sent-recover-password-email.html', data=data)


@app.route('/entrar', methods=['GET', 'POST'])
@log_route
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
        data = login_data_provider.get_data(form=form, msgs=msgs)
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
            msgs = [{
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
            }]
            data = login_data_provider.get_data(form=form, msgs=msgs)
            return render_template('user_management/login.html', data=data)

        if invalid_form:
            data = login_data_provider.get_data(form=form)
            return render_template('user_management/login.html', data=data)

        if not email_registered:
            data = login_data_provider.get_data(form=form)
            data["form"].email.errors.append("Email não registrado")
            return render_template('user_management/login.html', data=data)

        if not email_confirmed:
            data = login_data_provider.get_data(form=form)
            data["form"].email.errors.append(
                "Email não confirmado. Para reenviar o email de confirmação clique <a href='%s'>aqui</a>." % url_for(
                    "resend_confirmation_email"))
            return render_template('user_management/login.html', data=data)

        if incorrect_password:
            data = login_data_provider.get_data(form=form)
            data["form"].password.errors.append("Senha incorreta")
            return render_template('user_management/login.html', data=data)

        abort(404)


@app.route('/redefinir-senha/<token>', methods=["GET", "POST"])
@log_route
def redefine_password(token):
    try:
        email = ts.loads(token, salt="recover-key")
    except:
        abort(404)

    form = RedefinePasswordForm()

    if request.method == "GET":
        data = redefine_password_data_provider.get_data(form=form, email=email, token=token, msgs=[])
        return render_template('user_management/redefine-password.html', data=data)
    elif request.method == "POST":
        invalid_form = not form.validate_on_submit()

        if invalid_form:
            data = redefine_password_data_provider.get_data(form=form, email=email, token=token, msgs=[])
            return render_template('user_management/redefine-password.html', data=data)

        # Changing user password
        try:
            user = User.query.filter_by(email=email).first_or_404()
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            msgs = [{
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
            }]
            data = redefine_password_data_provider.get_data(form=form, email=email, token=token, msgs=msgs)
            return render_template('user_management/redefine-password.html', data=data)

        return redirect(url_for('login', msg_type="success", msg_content="Senha redefinida com sucesso."))
    return None


@app.route('/reenviar-email-de-confirmacao', methods=['GET', 'POST'])
@log_route
def resend_confirmation_email():
    form = EmailForm()
    if request.method == 'GET':
        data = resend_confirmation_email_data_provider.get_data(form)
        return render_template('user_management/resend-confirmation-email.html', data=data)
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
            msgs = [{
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao acessar o banco de dados. Tente novamente.",
            }]
            data = resend_confirmation_email_data_provider.get_data(form=form, msgs=msgs)
            return render_template('user_management/resend-confirmation-email.html', data=data)

        if invalid_form:
            data = resend_confirmation_email_data_provider.get_data(form=form)
            return render_template('user_management/resend-confirmation-email.html', data=data)

        if not email_registered:
            data = resend_confirmation_email_data_provider.get_data(form=form)
            data["form"].email.errors.append(
                "Email não registrado. Clique <a href='%s'>aqui</a> para criar uma nova conta." % url_for(
                    "create_account"))
            return render_template('user_management/resend-confirmation-email.html', data=data)

        if email_confirmed:
            data = resend_confirmation_email_data_provider.get_data(form=form)
            data["form"].email.errors.append(
                "Email já confirmado. Clique <a href='%s'>aqui</a> para entrar na conta." % url_for("login"))
            return render_template('user_management/resend-confirmation-email.html', data=data)

        # Sending confirmation message
        # TODO: Restrict the resend of the same email to one hour using a new table
        try:
            send_create_account_confirmation_email(form.email.data)
            return redirect(url_for("sent_confirmation_email", email=form.email.data))
        except:
            msgs = [{
                "type": "danger",
                "content": "Falha! Ocorreu um erro ao reenviar o email de confirmação. Tente novamente.",
            }]
            data = resend_confirmation_email_data_provider.get_data(form=form, msgs=msgs)
            return render_template('user_management/resend-confirmation-email.html', data=data)
    abort(404)


@app.route('/sair')
@login_required
@log_route
def logout():
    logout_user()
    return redirect(url_for('login'))
