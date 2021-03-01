import request_authorisation
import event_71
import pytest

'''

'''

def test_10():
    token = request_authorisation.authorisation()

    r = event_71.without_sorting_and_couriers(token)

    id_ = r['result']['id']

    assert id_ != None, 'Блок не был создан'

    number = "11-1111-1112"

    r = event_71.add_object(token, id_, number)

    assert r['metadata']['message'] == "Номер объекта не валидный: 11-1111-1112", 'Система не вернула ошибку «Номер объекта не валидный: 11-1111-1112»'