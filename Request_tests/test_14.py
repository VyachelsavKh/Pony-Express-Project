import request_authorisation
import event_79
import paths
import pytest

'''

'''

def test_14():
    token = request_authorisation.authorisation()

    destinationPointId = paths.destinationPointId_1202

    r = event_79.included_in_consolidation(token, destinationPointId)

    destinationPoint = r['result']['destinationPoint']

    assert destinationPoint['code'] == '1202', 'Попал в другой блок'

    id_ = r['result']['id']

    number = "99-9999-9999/999"

    r = event_79.add_object(token, id_, number)

    assert r['metadata']['message'] == "Отсутствует введенное место накладной", 'Система не вернула ошибку «Отсутствует введенное место накладной»'
