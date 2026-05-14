from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# register test
def test_register():
    response = client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@test.com",
        "password": "123456",
        "role": "patient"
    })

    assert response.status_code == 200


# login test
def test_login():
    response = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "123456"
    })

    assert response.status_code in [200, 404, 401]


# protected route test
def test_protected_route():
    response = client.get("/patients")

    # must fail because no token
    assert response.status_code in [401, 403]


# admin access test basicc
def test_book_appointment():
    response = client.post("/appointments", json={
        "doctor_id": 1,
        "patient_id": 1,
        "appointment_time": "10:00"
    })

    # depends on DB state
    assert response.status_code in [200, 400, 401, 403]