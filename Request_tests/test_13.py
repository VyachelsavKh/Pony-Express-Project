import request_authorisation
import event_79
import paths
import pytest

'''

'''


def test_13():
    token = request_authorisation.authorisation()

    destinationPointId = paths.destinationPointId_1202

    r = event_79.included_in_consolidation(token, destinationPointId)

    destinationPoint = r['result']['destinationPoint']

    assert destinationPoint['code'] == '1202', 'Попал в другой блок'
