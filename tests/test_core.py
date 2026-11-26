def test_inicio(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.get_json()["mensaje"] == "Sistema de ventas activo"


def test_crear_producto(client):
    r = client.post("/productos", json={"nombre": "Lapiz", "precio": 2.5})
    assert r.status_code == 201
    assert r.get_json()["nombre"] == "Lapiz"


def test_crear_producto_sin_precio(client):
    r = client.post("/productos", json={"nombre": "Lapiz"})
    assert r.status_code == 400
