import pytest
from webtest import TestApp
from app import setup_app

@pytest.fixture
def app():
    return setup_app()

@pytest.fixture
def webapp(app):
    return TestApp(app)
