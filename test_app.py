from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_success():
    response = client.post('/', json={"x": 1, "y": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_fail():
    response = client.post('/', json={"x": 0, "y": -1})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "x"
                ],
                "msg": "value must be a positive integer",
                "type": "value_error"
            },
            {
                "loc": [
                    "body",
                    "y"
                ],
                "msg": "value must be a non-negative integer",
                "type": "value_error"
            }
        ]
    }
