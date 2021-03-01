import request_authorisation
import event_71
import pytest

'''

'''

def test_8():
    token = request_authorisation.authorisation()

    r = event_71.without_sorting_and_couriers(token)

    assert r['result']['id'] != None, 'Блок не был создан'
