from itsdangerous import URLSafeTimedSerializer

from flask_app import app

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])