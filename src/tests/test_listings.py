from array import array
from typing import Generator
from fastapi.testclient import TestClient
from src.main import app
import pytest

@pytest.fixture
def client() -> Generator:
    with TestClient(app) as c:
        yield c

def test_get_listing_by_id(client):
    response = client.get('/api/v1/listings/1234')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Listing not found'}

def test_get_listings(client):
    response = client.get("/api/v1/listings")
    assert response.status_code == 200

def test_delete_listing(client):
    response = client.delete("/api/v1/listings/231")
    assert response.status_code == 404