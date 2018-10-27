from flask import Flask


def register_web_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_web_blueprint(app)
    return app
