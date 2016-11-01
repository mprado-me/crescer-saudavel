#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, url_for
from flask_app.utils.security import ts

from flask_mail import Message
from flask_app import app, mail

def send_create_account_confirmation_email(receiver_email):
	subject = "Confirme seu endereço de e-mail"
	token = ts.dumps(receiver_email, salt='email-confirm-key')
	confirm_url = url_for('email_confirmed', token=token, _external=True)
	logo_url = url_for('static', filename="images/logo.png", _external=True)
	data = {
		"confirm_url":confirm_url, 
		"logo_url":logo_url, 
		"email":receiver_email,
	}
	html=render_template("email/activate-account.html", data=data)
	msg = Message(sender=app.config["MAIL_USERNAME"], recipients=[receiver_email], subject=subject, html=html)
	try:
		mail.send(msg)
	except:
		raise