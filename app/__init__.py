from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    from app.core import productos, clientes, ventas

    app.register_blueprint(productos.bp)
    app.register_blueprint(clientes.bp)
    app.register_blueprint(ventas.bp)

    @app.route("/")
    def inicio():
        return jsonify({"mensaje": "Sistema de ventas activo"})

    return app
