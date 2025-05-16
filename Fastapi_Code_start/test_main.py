"""
Test file for FastAPI application
Checking the root or any endpoint
Is it working Correctly or not  
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": True, "message": "Hello World"}
