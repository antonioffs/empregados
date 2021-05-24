from flask import Flask
from empregado.database import close_db

from empregado.routes.empregado_routes import empregado_routes_blueprint
from empregado.routes.empregado_endereco_routes import empregado_end_routes_blueprint
from empregado.database import close_db

def create_app():

    app = Flask(__name__)
    app.register_blueprint(empregado_routes_blueprint)
    app.register_blueprint(empregado_end_routes_blueprint)
    return app
