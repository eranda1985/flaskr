import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from flaskr import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    #print(create_app({"VERSION": "Testing"}).config)
    assert create_app({"VERSION": "Testing"}).config['VERSION'] == "Testing"


def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"
