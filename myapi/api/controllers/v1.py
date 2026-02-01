from pecan import expose, rest

from pecan import expose, rest, request, response
from myapi.db import api as db_api

class ItemsController(rest.RestController):
    @expose(template='json')
    def get_one(self, item_id):
        # GET /v1/items/{item_id}
        item = db_api.get_item(item_id)
        if not item:
            response.status = 404
            return dict(error='Item not found')
        return dict(id=item.id, name=item.name)

    @expose(template='json')
    def get_all(self):
        # GET /v1/items
        items = db_api.get_items()
        return dict(items=[dict(id=i.id, name=i.name) for i in items])
        
    @expose(template='json')
    def post(self):
        # POST /v1/items/
        # pecan request body handling usually requires some care or use of @expose(generic=True)
        # For simplicity we assume JSON body is parsed or use request.json
        data = request.json
        item = db_api.create_item(name=data['name'])
        response.status = 201
        return dict(id=item.id, name=item.name)

class V1Controller(object):
    @expose(template='json')
    def index(self):
        return dict(status='v1_available')
    
    # Sub-controller for /v1/items
    items = ItemsController()
