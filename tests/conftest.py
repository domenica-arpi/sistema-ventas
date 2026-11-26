import pytest

from app import create_app
from app.core import clientes, productos, ventas


@pytest.fixture
def client():
    productos.PRODUCTOS.clear()
    clientes.CLIENTES.clear()
    ventas.VENTAS.clear()
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
