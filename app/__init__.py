from flask import Flask
from flask_login import LoginManager
from app.models.base import db


login_manager = LoginManager()


def register_web_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_web_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app
