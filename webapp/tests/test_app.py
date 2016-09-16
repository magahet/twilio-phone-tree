from app import app
from nose.tools import (eq_, ok_)


def test_gather():
    test_app = app.test_client()
    response = test_app.get('/')
    eq_(response.status, '200 OK')
    eq_(response.data, '')
