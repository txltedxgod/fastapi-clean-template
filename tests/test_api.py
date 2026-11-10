"""Integration tests for user lifecycle API, middleware tracing, and error handling."""

from fastapi.testclient import TestClient


def test_user_lifecycle(client: TestClient) -> None:
    res = client.post(
        "/api/v1/users",
        json={"email": "dev@company.io", "full_name": "Dev User", "role": "admin"},
    )
    assert res.status_code == 201
    user_id = res.json()["id"]

    get_res = client.get(f"/api/v1/users/{user_id}")
    assert get_res.status_code == 200
    assert get_res.json()["email"] == "dev@company.io"

    del_res = client.delete(f"/api/v1/users/{user_id}")
    assert del_res.status_code == 204
    assert client.get(f"/api/v1/users/{user_id}").status_code == 404


def test_correlation_id_middleware_and_health(client: TestClient) -> None:
    health = client.get("/health", headers={"X-Correlation-ID": "trace-abc-123"})
    assert health.status_code == 200
    assert health.json()["status"] == "healthy"
    assert health.headers["X-Correlation-ID"] == "trace-abc-123"
    assert "X-Response-Time-Ms" in health.headers

    generated = client.get("/health")
    assert generated.status_code == 200
    assert len(generated.headers["X-Correlation-ID"]) >= 8


def test_duplicate_email_conflict_and_pagination(client: TestClient) -> None:
    payload = {"email": "dup@company.io", "full_name": "First", "role": "member"}
    assert client.post("/api/v1/users", json=payload).status_code == 201

    conflict = client.post(
        "/api/v1/users",
        json={"email": "DUP@company.io", "full_name": "Second", "role": "member"},
    )
    assert conflict.status_code == 409
    assert conflict.json()["error"]["type"] == "DuplicateResourceError"

    assert (
        client.post(
            "/api/v1/users",
            json={"email": "second@company.io", "full_name": "Two", "role": "member"},
        ).status_code
        == 201
    )
    page = client.get("/api/v1/users?limit=1&offset=1")
    assert page.status_code == 200
    assert len(page.json()) == 1
    assert page.json()[0]["email"] == "second@company.io"
