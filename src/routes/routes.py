from flask import Flask
from .user import user_routes_bp
from .machine import machine_routes_bp
from .node import node_routes_bp


def register_routes(app: Flask):
    app.register_blueprint(user_routes_bp, url_prefix='/user')
    app.register_blueprint(machine_routes_bp, url_prefix='/machine')
    app.register_blueprint(node_routes_bp, url_prefix='/node')
