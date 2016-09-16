from app import app
from nose.tools import (eq_, ok_)


def test_gather_root():
    test_app = app.test_client()
    response = test_app.post('/')
    eq_(response.status, '200 OK')
    expected = (
        '<?xml version="1.0" encoding="UTF-8"?>'
            '<Response>'
                '<Gather action="/eyJjaG9pY2VzIjogW119" method="POST" numDigits="1">'
                '<Say loop="3">'
                    'To reach Group 1 press 0. To reach Person 3 press 1. To reach Person 4 press 2.'
                '</Say>'
                '</Gather>'
            '</Response>'
    )
    eq_(response.data, expected)


def test_gather_group_0():
    test_app = app.test_client()
    response = test_app.post('/eyJjaG9pY2VzIjogW251bGxdfQ==', data={'Digits': 0})
    eq_(response.status, '200 OK')
    expected = (
        '<?xml version="1.0" encoding="UTF-8"?>'
            '<Response>'
                '<Gather action="/eyJjaG9pY2VzIjogW251bGwsIDBdfQ==" method="POST" numDigits="1">'
                '<Say loop="3">'
                    'To reach Person 1 press 0. To reach Person 2 press 1.'
                '</Say>'
                '</Gather>'
            '</Response>'
    )

    eq_(response.data, expected)
