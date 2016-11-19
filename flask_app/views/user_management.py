#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, redirect, render_template, request, url_for
from flask_app.data_providers.customer.user_management.create_account import create_account_data_provider
from flask_app.data_providers.customer.user_management.login import login_data_provider
from flask_app.data_providers.customer.user_management.recover_password import recover_password_data_provider
from flask_app.data_providers.customer.user_management.redefine_password import redefine_password_data_provider
from flask_app.data_providers.customer.user_management.resend_confirmation_email import resend_confirmation_email_data_provider
from flask_app.data_providers.customer.user_management.sent_confirmation_email import sent_confirmation_email_data_provider
from flask_app.data_providers.customer.user_management.sent_recover_password_email import sent_recover_password_email_data_provider
from flask_login import login_required, login_user, logout_user
from itsdangerous import BadSignature

from flask_app.data_providers.customer.general.failed_to_get import failed_to_get_data_provider
from .. import app
from ..forms.user import CreateAccountForm, LoginForm, ResendConfirmationEmailForm, RecoverPasswordForm, RedefinePasswordForm
from ..models.user import User
from ..utils.db_manager import db_manager
from ..utils.decorators import log_route
from ..utils.email_manager import email_manager
from ..utils.exceptions import DatabaseAccessError, EmailSendingError, log_exception, log_unrecognized_exception
from ..utils.security import ts


@app.route('/email-de-confirmacao-enviado/<string:email>')
@log_route
def sent_confirmation_email(email):
    data = sent_confirmation_email_data_provider.get_data(email)
    return render_template("user_management/sent-confirmation-email.html", data=data)


@app.route('/criar-conta', methods=['GET', 'POST'])
@log_route
def create_account():
    form = CreateAccountForm()

    # GET
    if request.method == "GET":
        try:
            data = create_account_data_provider.get_data(form)
            return render_template('user_management/create-account.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = create_account_data_provider.get_data(form)
                return render_template('user_management/create-account.html', data=data)

            user = User(
                email=form.email.data,
                password=form.password.data
            )
            db_manager.add_user(user)

            email_manager.send_create_account_confirmation_email(form.email.data)

            db_manager.commit()
            return redirect(url_for("sent_confirmation_email", email=request.form["email"]))
        except DatabaseAccessError:
            db_manager.rollback()
            data = create_account_data_provider.get_data_when_database_access_error(form=form)
            return render_template('user_management/create-account.html', data=data)
        except EmailSendingError:
            data = create_account_data_provider.get_data_when_email_sending_error(form=form)
            return render_template('user_management/create-account.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


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
    except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/recuperar-senha', methods=["GET", "POST"])
@log_route
def recover_password():
    form = RecoverPasswordForm()

    # GET
    if request.method == "GET":
        try:
            data = recover_password_data_provider.get_data(form=form)
            return render_template('user_management/recover-password.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = recover_password_data_provider.get_data(form=form)
                return render_template('user_management/recover-password.html', data=data)

            email_manager.send_redefine_password_email(form.email.data)
            return redirect(url_for("sent_recover_password_email", email=form.email.data))
        except DatabaseAccessError:
            data = recover_password_data_provider.get_data_when_database_access_error(form=form)
            return render_template('user_management/recover-password.html', data=data)
        except EmailSendingError:
            data = recover_password_data_provider.get_data_when_email_sending_error(form=form)
            return render_template('user_management/recover-password.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/email-de-recuperacao-de-senha-enviado/<string:email>')
@log_route
def sent_recover_password_email(email):
    try:
        data = sent_recover_password_email_data_provider.get_data(email=email)
        return render_template('user_management/sent-recover-password-email.html', data=data)
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)


@app.route('/entrar', methods=['GET', 'POST'])
@log_route
def login():
    form = LoginForm()

    # GET
    if request.method == "GET":
        try:
            data = login_data_provider.get_data_when_get_request(form=form)
            return render_template('user_management/login.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = login_data_provider.get_data(form=form)
                return render_template('user_management/login.html', data=data)

            user = db_manager.get_user(form.email.data)
            user.authenticated = True
            db_manager.add_user(user)
            db_manager.commit()
            login_user(user)
            return redirect(url_for('my_account'))
        except DatabaseAccessError:
            db_manager.rollback()
            data = login_data_provider.get_data_when_database_access_error(form=form)
            return render_template('user_management/login.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/redefinir-senha/<token>', methods=["GET", "POST"])
@log_route
def redefine_password(token):
    form = RedefinePasswordForm()

    # GET
    if request.method == "GET":
        try:
            email = ts.loads(token, salt="recover-key")
            data = redefine_password_data_provider.get_data(form=form, email=email, token=token)
            return render_template('user_management/redefine-password.html', data=data)
        except BadSignature:
            log_exception(name="BadSignature")
            abort(404)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        email = None
        try:
            email = ts.loads(token, salt="recover-key")

            if not form.validate_on_submit():
                data = redefine_password_data_provider.get_data(form=form, email=email, token=token)
                return render_template('user_management/redefine-password.html', data=data)

            user = db_manager.get_user(email)
            user.password = form.password.data
            db_manager.add_user(user)
            db_manager.commit()

            return redirect(url_for('login', msg_type="success", msg_content="Senha redefinida com sucesso."))
        except BadSignature:
            log_exception(name="BadSignature")
            abort(404)
        except DatabaseAccessError:
            db_manager.rollback()
            data = redefine_password_data_provider.get_data_when_database_access_error(form=form, email=email, token=token)
            return render_template('user_management/redefine-password.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/reenviar-email-de-confirmacao', methods=['GET', 'POST'])
@log_route
def resend_confirmation_email():
    form = ResendConfirmationEmailForm()

    # GET
    if request.method == 'GET':
        try:
            data = resend_confirmation_email_data_provider.get_data(form)
            return render_template('user_management/resend-confirmation-email.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = resend_confirmation_email_data_provider.get_data(form=form)
                return render_template('user_management/resend-confirmation-email.html', data=data)

            # TODO: Wait one hour to resend for the same email
            email_manager.send_create_account_confirmation_email(form.email.data)
            return redirect(url_for("sent_confirmation_email", email=form.email.data))
        except DatabaseAccessError:
            data = resend_confirmation_email_data_provider.get_data_when_database_access_error(form=form)
            return render_template('user_management/resend-confirmation-email.html', data=data)
        except EmailSendingError:
            data = resend_confirmation_email_data_provider.get_data_when_email_sending_error(form=form)
            return render_template('user_management/resend-confirmation-email.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)


@app.route('/sair')
@login_required
@log_route
def logout():
    try:
        logout_user()
        return redirect(url_for('login'))
    except Exception as e:
        log_unrecognized_exception(e)
        abort(500)
