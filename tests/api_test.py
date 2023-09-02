from __future__ import annotations

from fastapi.testclient import TestClient
from fib.main import app

client = TestClient(app)


def test_read_index():
    resp = client.get('/?n=7')
    assert resp.status_code == 200
    assert resp.json() == 13


def test_bad_request():
    resp = client.get('/?n=-7')
    assert resp.status_code == 400
    assert resp.json()['detail'] == 'Enter Integer!'
