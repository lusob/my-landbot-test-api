from app_factory import create_app
from models import db
import utils
import pytest

app, mail_server = create_app("test_app.cfg")


def setup_function(function):
    print("Creating db test")
    with app.app_context():
        db.create_all()


def teardown_function(function):
    print("Dropping db test")
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def remove_time_delay(monkeypatch):
    monkeypatch.setattr(
        utils,
        "send_deferred_email",
        lambda mail, user_name, user_email: utils._send_deferred_email(
            mail, user_name, user_email, seconds=0
        ),
    )


def test_user(client, remove_time_delay):
    # Check user is saved and mail is sent
    with mail_server.record_messages() as outbox:
        response = client.post(
            "/user", data=dict(name="tester", email="test@example.com")
        )
        json = response.get_json()
        assert json["User"] == "tester"
        assert len(outbox) == 1
        assert outbox[0].subject == "Welcome tester"


def test_not_found(client):
    response = client.get("/wrong-url")
    json = response.get_json()
    assert response.content_type == "application/json"
    assert response.status_code == 404
    assert json["error"] == "404 Not Found"
