from fastapi.testclient import TestClient

from api.index import app


def test_root_ok():
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

