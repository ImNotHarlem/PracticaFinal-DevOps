from app import app

def test_inicio():
    cliente = app.test_client()
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert respuesta.data == b"Hola Mundo - Examen Final DevOps"