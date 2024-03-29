from .. import app

from flask import request, redirect, session, url_for

from functools import wraps

def admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session["user_id"] != app.config['ADMIN_MAIL']:
            return redirect(url_for('home'))
        return func(*args, **kwargs)

    return decorated_function

def log_route(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        app.logger.debug("-*-*-")
        app.logger.debug(str(func.__name__) + " | " + request.method)
        if len(kwargs) > 0:
            app.logger.debug("url_params: " + str(kwargs))
        query_params = dict(request.args)
        if len(query_params) > 0:
            app.logger.debug("query_params: " + str(query_params))
        if request.method == "POST" and len(request.form) > 0:
            post_params = dict(request.form)
            if "password" in post_params:
                post_params["password"] = "******"
            if "password_confirmation" in post_params:
                post_params["password_confirmation"] = "******"
            app.logger.debug("post_params: " + str(post_params))
        return func(*args, **kwargs)
    return decorated_function
