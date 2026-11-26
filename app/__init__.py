from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    from app.core import productos, clientes

    app.register_blueprint(productos.bp)
    app.register_blueprint(clientes.bp)

    @app.route("/")
    def inicio():
        return jsonify({"mensaje": "Sistema de ventas activo"})

    return app
