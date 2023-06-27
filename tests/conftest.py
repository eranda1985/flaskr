import os
import sys
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from flaskr import create_app


@pytest.fixture
def app():
    # create the app with common test config
    app = create_app({"VERSION": "Testing"})
    yield app


@pytest.fixture
def client(app):
    # create a test client for the app.
    return app.test_client()
