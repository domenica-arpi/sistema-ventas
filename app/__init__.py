from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def inicio():
        return jsonify({"mensaje": "Sistema de ventas activo"})

    return app
