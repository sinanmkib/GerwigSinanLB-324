import os
import pytest

# Test-ENV HART setzen (überschreibt CI-ENV sicher)
os.environ["PASSWORD"] = "test123"
os.environ["SECRET_KEY"] = "testsecret"

from app import app, entries  # noqa: E402


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    # pro Testlauf Liste leeren, damit Indizes stimmen
    entries.clear()
    with app.test_client() as c:
        yield c


def login(client, pw="test123"):
    return client.post("/login", data={"password": pw}, follow_redirects=True)


def test_index_ok(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_add_requires_login(client):
    resp = client.post("/add_entry", data={"content": "Hallo"})
    assert resp.status_code in (302, 308)
    assert "/login" in resp.headers.get("Location", "")


def test_add_after_login_redirects_to_index(client):
    login(client)
    resp = client.post("/add_entry", data={"content": "Test Entry Content"})
    assert resp.status_code in (302, 308)
    assert resp.headers.get("Location", "").endswith("/")


def test_entry_visible_after_login(client):
    login(client)
    resp = client.post("/add_entry", data={"content": "Visible"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Visible" in resp.data


def test_add_entry_with_happiness(client):
    # Vorgabe der LB
    login(client)  # wir loggen ein, sonst redirect auf /login
    response = client.post(
        "/add_entry",
        data={"content": "Test Entry Content", "happiness": "😃"},
        follow_redirects=False,
    )
    # Redirect auf Index
    assert response.status_code in (302, 308)
    assert response.headers.get("Location", "") == "/"

    # Eintrag mit Happiness korrekt gespeichert
    entry = entries[0]
    assert entry is not None
    assert entry.content == "Test Entry Content"
    assert entry.happiness == "😃"
