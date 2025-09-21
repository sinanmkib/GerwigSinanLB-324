import os
import pytest

# Test-ENV setzen (falls .env nicht geladen wird)
os.environ.setdefault("PASSWORD", "test123")
os.environ.setdefault("SECRET_KEY", "testsecret")

from app import app  # noqa: E402  (nach ENV-Setup importieren)


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def login(client, pw="test123"):
    return client.post("/login", data={"password": pw}, follow_redirects=True)


def test_index_ok(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_add_requires_login(client):
    resp = client.post("/add_entry", data={"content": "Hallo"})
    # ohne Login ⇒ Redirect zur Login-Seite
    assert resp.status_code in (302, 308)
    assert "/login" in resp.headers.get("Location", "")


def test_add_after_login_redirects_to_index(client):
    # erst einloggen
    r = login(client)
    assert r.status_code == 200

    # dann Eintrag hinzufügen
    resp = client.post("/add_entry", data={"content": "Test Entry Content"})
    # jetzt Redirect zurück zur Startseite
    assert resp.status_code in (302, 308)
    assert resp.headers.get("Location", "").endswith("/")


def test_entry_visible_after_login(client):
    login(client)
    resp = client.post("/add_entry", data={"content": "Visible"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Visible" in resp.data
