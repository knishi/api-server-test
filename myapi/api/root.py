from pecan import expose
from myapi.api.controllers import v1

class RootController(object):
    @expose(generic=True, template='json')
    def index(self):
        return dict(status='running', versions=['v1'])

    # Sub-controller for /v1
    v1 = v1.V1Controller()
