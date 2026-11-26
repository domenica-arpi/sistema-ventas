from flask import Blueprint, jsonify, request

bp = Blueprint("clientes", __name__)

CLIENTES = []


@bp.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(CLIENTES)


@bp.route("/clientes", methods=["POST"])
def crear_cliente():
    datos = request.get_json()
    if not datos or "nombre" not in datos or "correo" not in datos:
        return jsonify({"error": "nombre y correo son obligatorios"}), 400
    cliente = {
        "id": len(CLIENTES) + 1,
        "nombre": datos["nombre"],
        "correo": datos["correo"],
    }
    CLIENTES.append(cliente)
    return jsonify(cliente), 201
