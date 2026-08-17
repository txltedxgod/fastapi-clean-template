def test_user_lifecycle(client):
    res = client.post("/api/v1/users", json={"email": "dev@company.io", "full_name": "Dev User", "role": "admin"})
    assert res.status_code == 201
    user_id = res.json()["id"]
    get_res = client.get(f"/api/v1/users/{user_id}")
    assert get_res.status_code == 200
    assert get_res.json()["email"] == "dev@company.io"
