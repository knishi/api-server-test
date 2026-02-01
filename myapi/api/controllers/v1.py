from pecan import expose, rest

class ItemsController(rest.RestController):
    @expose(template='json')
    def get_one(self, item_id):
        # GET /v1/items/{item_id}
        return dict(id=item_id, name=f'Item {item_id}')

    @expose(template='json')
    def get_all(self):
        # GET /v1/items
        return dict(items=[dict(id=1, name='Item 1'), dict(id=2, name='Item 2')])

class V1Controller(object):
    @expose(template='json')
    def index(self):
        return dict(status='v1_available')
    
    # Sub-controller for /v1/items
    items = ItemsController()
