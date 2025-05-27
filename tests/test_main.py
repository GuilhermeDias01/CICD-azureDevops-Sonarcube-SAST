from app import create_app

def test_index():
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'Olá, mundo!'
