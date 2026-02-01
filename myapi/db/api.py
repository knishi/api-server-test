from oslo_config import cfg
from oslo_db.sqlalchemy import enginefacade
from myapi.db import models

CONF = cfg.CONF

# Define the engine facade
_context_manager = enginefacade.transaction_context()

def get_engine():
    return _context_manager.writer.get_engine()

def setup_db():
    engine = get_engine()
    models.Base.metadata.create_all(engine)
    return engine
