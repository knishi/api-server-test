def test_get_root(webapp):
    resp = webapp.get('/')
    assert resp.status_int == 200
    assert resp.json['status'] == 'running'
    assert 'v1' in resp.json['versions']

def test_get_v1_index(webapp):
    resp = webapp.get('/v1/')
    assert resp.status_int == 200
    assert resp.json['status'] == 'v1_available'

def test_get_items(webapp):
    resp = webapp.get('/v1/items/')
    assert resp.status_int == 200
    assert len(resp.json['items']) == 2
    assert resp.json['items'][0]['name'] == 'Item 1'

def test_get_item_detail(webapp):
    resp = webapp.get('/v1/items/123')
    assert resp.status_int == 200
    assert resp.json['id'] == '123'
    assert resp.json['name'] == 'Item 123'
