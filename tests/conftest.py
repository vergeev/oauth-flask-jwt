import pytest

import wsgi


@pytest.fixture
def app():
    return wsgi.create_app()
