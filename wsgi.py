from flask import Flask

from oauth_flask_jwt.models import db
from oauth_flask_jwt.views import auth


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.register_blueprint(auth)
    db.init_app(app)
    return app
