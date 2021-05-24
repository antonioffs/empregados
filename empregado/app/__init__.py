from flask import Flask, signals, jsonify
from empregado.database import close_db

# from shortener.short_url import shorturl_blueprint
# from shortener.redirect import redirect_blueprint
from empregado.routes import routes_blueprint
from empregado.database import close_db
# from shortener.config import get_logger

def create_app():

    app = Flask(__name__)
    # app.register_blueprint(shorturl_blueprint)
    # app.register_blueprint(redirect_blueprint)
    app.register_blueprint(routes_blueprint)
    # Swagger(app, template=template, config=swagger_config)
    # signals.request_finished.connect(close_db, sender=app)
    return app
