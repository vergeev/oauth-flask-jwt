import pytest
from flask import url_for
from flask.testing import FlaskClient


@pytest.mark.xfail
def test_register(client: FlaskClient) -> None:
    response = client.post(url_for("auth.register"))
    assert response.status_code == 200
