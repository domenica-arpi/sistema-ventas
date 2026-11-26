from flask import Blueprint, jsonify, request

bp = Blueprint("productos", __name__)

PRODUCTOS = []


@bp.route("/productos", methods=["GET"])
def listar_productos():
    return jsonify(PRODUCTOS)


@bp.route("/productos", methods=["POST"])
def crear_producto():
    datos = request.get_json()
    if not datos or "nombre" not in datos or "precio" not in datos:
        return jsonify({"error": "nombre y precio son obligatorios"}), 400
    producto = {
        "id": len(PRODUCTOS) + 1,
        "nombre": datos["nombre"],
        "precio": datos["precio"],
    }
    PRODUCTOS.append(producto)
    return jsonify(producto), 201
