from fastapi.testclient import TestClient

from app.main import app


def test_inherits_valid_request_id() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/health", headers={"X-Request-ID": "req_custom-1"})
    assert response.headers["x-request-id"] == "req_custom-1"


def test_replaces_invalid_request_id() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/health", headers={"X-Request-ID": "invalid id"})
    assert response.headers["x-request-id"].startswith("req_")
