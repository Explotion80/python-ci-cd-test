import pytest
from app import app, add

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Calculator' in rv.data

def test_calculate(client):
    rv = client.post('/calculate', data=dict(a='2', b='3'))
    assert rv.status_code == 200
    assert b'Result: 2.0 + 3.0 = 5.0' in rv.data