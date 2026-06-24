from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "operational"

def test_analyze_sos_high_urgency():
    payload = {
        "text": "We are trapped in the flood on the roof!",
        "latitude": 34.0522,
        "longitude": -118.2437
    }
    response = client.post("/api/v1/analyze-sos", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["urgency_level"] == "HIGH"
    assert data["dispatch_recommended"] == True

def test_analyze_sos_low_urgency():
    payload = {
        "text": "The power is out but everyone is safe.",
        "latitude": 34.0522,
        "longitude": -118.2437
    }
    response = client.post("/api/v1/analyze-sos", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["urgency_level"] == "LOW"
    assert data["dispatch_recommended"] == False
