from flask import Blueprint, jsonify, request

from app.core.clientes import CLIENTES
from app.core.productos import PRODUCTOS

bp = Blueprint("ventas", __name__)

VENTAS = []


@bp.route("/ventas", methods=["GET"])
def listar_ventas():
    return jsonify(VENTAS)


@bp.route("/ventas", methods=["POST"])
def crear_venta():
    datos = request.get_json()
    campos = ("producto_id", "cliente_id", "cantidad")
    if not datos or any(c not in datos for c in campos):
        return jsonify({"error": "producto_id, cliente_id y cantidad son obligatorios"}), 400
    producto = next((p for p in PRODUCTOS if p["id"] == datos["producto_id"]), None)
    cliente = next((c for c in CLIENTES if c["id"] == datos["cliente_id"]), None)
    if producto is None or cliente is None:
        return jsonify({"error": "producto o cliente no existe"}), 404
    venta = {
        "id": len(VENTAS) + 1,
        "producto_id": producto["id"],
        "cliente_id": cliente["id"],
        "cantidad": datos["cantidad"],
        "total": producto["precio"] * datos["cantidad"],
    }
    VENTAS.append(venta)
    return jsonify(venta), 201
