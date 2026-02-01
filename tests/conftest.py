import pytest
from webtest import TestApp
from app import setup_app

@pytest.fixture
def app():
    from oslo_config import cfg
    from oslo_db import options
    from myapi.db import api
    
    # Configure DB for tests
    options.set_defaults(cfg.CONF, connection='sqlite:///:memory:')
    api.setup_db()
    
    return setup_app()

@pytest.fixture
def webapp(app):
    return TestApp(app)
