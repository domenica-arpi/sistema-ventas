def test_crear_cliente(client):
    r = client.post("/clientes", json={"nombre": "Ana", "correo": "ana@mail.com"})
    assert r.status_code == 201
    assert r.get_json()["correo"] == "ana@mail.com"


def test_crear_venta_calcula_total(client):
    client.post("/productos", json={"nombre": "Lapiz", "precio": 2.5})
    client.post("/clientes", json={"nombre": "Ana", "correo": "ana@mail.com"})
    r = client.post("/ventas", json={"producto_id": 1, "cliente_id": 1, "cantidad": 4})
    assert r.status_code == 201
    assert r.get_json()["total"] == 10.0
