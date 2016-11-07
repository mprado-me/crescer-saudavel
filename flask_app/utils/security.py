from .. import app

from itsdangerous import URLSafeTimedSerializer

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])