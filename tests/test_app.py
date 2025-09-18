# Write pytest tests for the FastAPI app in src/app.py
# - test_health() should check {"status": "ok"}
# - test_sum() should check sum of a and b for a couple of cases
# Use TestClient from fastapi

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    """Test the /health endpoint returns status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_sum(a: int, b: int, expected: int):
    """Test the /sum endpoint returns correct sum for various cases."""
    response = client.get(f"/sum?a={a}&b={b}")
    assert response.status_code == 200
    assert response.json() == {"sum": expected}
