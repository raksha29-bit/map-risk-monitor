from fastapi.testclient import TestClient
from backend.app.main import app


client = TestClient(app)

def test_evaluate_endpoint_exists():
    response = client.post(
        "/api/evaluate",
        params={
            "location": "Zone 5",
            "query": "AQI rising"
        }
    )

    assert response.status_code == 200
