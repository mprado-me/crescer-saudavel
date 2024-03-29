#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, flash, redirect, render_template, request, url_for
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
from flask_app import app
from flask_app.forms.user import CreateAccountForm, LoginForm, ResendConfirmationEmailForm, RecoverPasswordForm, RedefinePasswordForm
from flask_app.models.user import User
from flask_app.utils.db_manager import db_manager
from flask_app.utils.decorators import log_route
from flask_app.utils.email_manager import email_manager
from flask_app.utils.exceptions import DatabaseAccessError, EmailSendingError, log_exception, log_unrecognized_exception
from flask_app.utils.security import ts


@app.route('/email-de-confirmacao-enviado/<string:email>')
@log_route
def sent_confirmation_email(email):
    data = sent_confirmation_email_data_provider.get_data(email)
    return render_template("customer/user_management/sent-confirmation-email.html", data=data)


@app.route('/criar-conta', methods=['GET', 'POST'])
@log_route
def create_account():
    form = CreateAccountForm()

    # GET
    if request.method == "GET":
        try:
            data = create_account_data_provider.get_data(form)
            return render_template('customer/user_management/create-account.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = create_account_data_provider.get_data(form)
                return render_template('customer/user_management/create-account.html', data=data)

            user = User(
                email=form.email.data,
                password=form.password.data
            )
            db_manager.add(user)

            email_manager.send_create_account_confirmation_email(form.email.data)

            db_manager.commit()
            return redirect(url_for("sent_confirmation_email", email=request.form["email"]))
        except DatabaseAccessError:
            db_manager.rollback()
            flash(DatabaseAccessError.msg, "danger")
            data = create_account_data_provider.get_data(form=form)
            return render_template('customer/user_management/create-account.html', data=data)
        except EmailSendingError:
            db_manager.rollback()
            flash(EmailSendingError.msg, "danger")
            data = create_account_data_provider.get_data(form=form)
            return render_template('customer/user_management/create-account.html', data=data)
        except Exception as e:
            db_manager.rollback()
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
        db_manager.add(user)
        db_manager.commit()
        flash("Email confirmado com sucesso.", "success")
        return redirect(url_for('login'))
    except BadSignature:
        db_manager.rollback()
        log_exception(name="BadSignature")
        abort(404)
    except DatabaseAccessError:
        db_manager.rollback()
        current_url = url_for('email_confirmed', token=token)
        flash(DatabaseAccessError.msg, "danger")
        data = failed_to_get_data_provider.get_data(current_url=current_url)
        return render_template('customer/shared/failed-to-get.html', data=data)
    except Exception as e:
        db_manager.rollback()
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
            return render_template('customer/user_management/recover-password.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = recover_password_data_provider.get_data(form=form)
                return render_template('customer/user_management/recover-password.html', data=data)

            email_manager.send_redefine_password_email(form.email.data)
            return redirect(url_for("sent_recover_password_email", email=form.email.data))
        except DatabaseAccessError:
            db_manager.rollback()
            flash(DatabaseAccessError.msg, "danger")
            data = recover_password_data_provider.get_data(form=form)
            return render_template('customer/user_management/recover-password.html', data=data)
        except EmailSendingError:
            db_manager.rollback()
            flash(EmailSendingError.msg, "danger")
            data = recover_password_data_provider.get_data(form=form)
            return render_template('customer/user_management/recover-password.html', data=data)
        except Exception as e:
            db_manager.rollback()
            log_unrecognized_exception(e)
            abort(500)


@app.route('/email-de-recuperacao-de-senha-enviado/<string:email>')
@log_route
def sent_recover_password_email(email):
    try:
        data = sent_recover_password_email_data_provider.get_data(email=email)
        return render_template('customer/user_management/sent-recover-password-email.html', data=data)
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
            data = login_data_provider.get_data(form=form)
            return render_template('customer/user_management/login.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = login_data_provider.get_data(form=form)
                return render_template('customer/user_management/login.html', data=data)

            user = db_manager.get_user(form.email.data)
            user.authenticated = True
            db_manager.add(user)
            db_manager.commit()
            login_user(user)

            if user.email == app.config["ADMIN_MAIL"]:
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('my_account'))
        except DatabaseAccessError:
            db_manager.rollback()
            flash(DatabaseAccessError.msg, "danger")
            data = login_data_provider.get_data(form=form)
            return render_template('customer/user_management/login.html', data=data)
        except Exception as e:
            db_manager.rollback()
            log_unrecognized_exception(e)
            abort(500)


# TODO: Add a time constraint to the token
@app.route('/redefinir-senha/<token>', methods=["GET", "POST"])
@log_route
def redefine_password(token):
    form = RedefinePasswordForm()

    # GET
    if request.method == "GET":
        try:
            email = ts.loads(token, salt="recover-key")
            data = redefine_password_data_provider.get_data(form=form, email=email, token=token)
            return render_template('customer/user_management/redefine-password.html', data=data)
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
                return render_template('customer/user_management/redefine-password.html', data=data)

            user = db_manager.get_user(email)
            user.password = form.password.data
            db_manager.add(user)
            db_manager.commit()

            flash("Senha redefinida com sucesso.", "success")
            return redirect(url_for('login'))
        except BadSignature:
            db_manager.rollback()
            log_exception(name="BadSignature")
            abort(404)
        except DatabaseAccessError:
            db_manager.rollback()
            flash(DatabaseAccessError.msg, "danger")
            data = redefine_password_data_provider.get_data(form=form, email=email, token=token)
            return render_template('customer/user_management/redefine-password.html', data=data)
        except Exception as e:
            db_manager.rollback()
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
            return render_template('customer/user_management/resend-confirmation-email.html', data=data)
        except Exception as e:
            log_unrecognized_exception(e)
            abort(500)

    # POST
    else:
        try:
            if not form.validate_on_submit():
                data = resend_confirmation_email_data_provider.get_data(form=form)
                return render_template('customer/user_management/resend-confirmation-email.html', data=data)

            # TODO: Wait one hour to resend for the same email
            email_manager.send_create_account_confirmation_email(form.email.data)
            return redirect(url_for("sent_confirmation_email", email=form.email.data))
        except DatabaseAccessError:
            db_manager.rollback()
            flash(DatabaseAccessError.msg, "danger")
            data = resend_confirmation_email_data_provider.get_data(form=form)
            return render_template('customer/user_management/resend-confirmation-email.html', data=data)
        except EmailSendingError:
            db_manager.rollback()
            flash(EmailSendingError.msg, "danger")
            data = resend_confirmation_email_data_provider.get_data(form=form)
            return render_template('customer/user_management/resend-confirmation-email.html', data=data)
        except Exception as e:
            db_manager.rollback()
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
