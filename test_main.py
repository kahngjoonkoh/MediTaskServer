from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

dummy_appointment_json = {
    "patient_name": "John Smith",
    "doctor_name": "Dr. Placeholder",
    "date": "18/07/2024",
    "time": "12:09",
}


def test_create_appointment_main():
    response = client.post("/appointments", json=dummy_appointment_json)
    assert response.status_code == 200
    assert response.json() is None


def test_get_all_appointments_main():
    response = client.get("/appointments")
    assert response.status_code == 200
    last_appointment = response.json()[-1]
    del last_appointment["id"]
    assert last_appointment == dummy_appointment_json


def test_get_single_appointment_main():
    response = client.get("/appointments")
    assert response.status_code == 200
    object_id = response.json()[-1]["id"]

    response = client.get(f"/appointments/{object_id}")
    assert response.status_code == 200
    appointment = response.json()
    del appointment["id"]
    assert appointment == dummy_appointment_json


def test_delete_single_appointment_main():
    response = client.get("/appointments")
    assert response.status_code == 200
    object_id = response.json()[-1]["id"]

    response = client.delete(f"/appointments/{object_id}")
    assert response.status_code == 200
    assert response.json() is None
