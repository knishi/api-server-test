import os
import pecan
from oslo_config import cfg

# Define oslo.config options if needed (example)
opt_group = cfg.OptGroup(name='api', title='API Options')
api_opts = [
    cfg.StrOpt('host_ip', default='0.0.0.0', help='The IP address to bind to.'),
    cfg.IntOpt('port', default=8080, help='The port to bind to.'),
]

CONF = cfg.CONF
CONF.register_group(opt_group)
CONF.register_opts(api_opts, group=opt_group)

def get_pecan_config():
    # In a real OpenStack app, we might mix oslo.config and pecan config
    # For simplicity, we load the python config file
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.py'))
    return pecan.configuration.conf_from_file(filename)

def setup_app(config=None):
    if not config:
        config = get_pecan_config()

    # Setup logging
    from oslo_log import log as logging
    from oslo_config import cfg
    logging.register_options(cfg.CONF)
    logging.setup(cfg.CONF, 'myapi')

    # Register hooks
    from myapi.common import hooks
    app_hooks = [hooks.ErrorHook()]

    app = pecan.make_app(
        config.app.root,
        static_root=config.app.static_root,
        template_path=config.app.template_path,
        debug=config.app.debug,
        hooks=app_hooks,
        force_canonical=getattr(config.app, 'force_canonical', True)
    )
    
    # Wrap with Keystone-compatible middleware
    from myapi.middleware import FakeAuthMiddleware
    app = FakeAuthMiddleware(app)
    
    return app

# WSGI Application for Gunicorn
application = setup_app()
