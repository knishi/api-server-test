from pecan.hooks import TransactionHook, RequestViewerHook

# Server Specific Configurations
server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'myapi.api.root.RootController',
    'modules': ['myapi.api'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/myapi/api/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}
