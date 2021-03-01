import request_authorisation
import gepgraphy

'''

'''

def test_16():
    token = request_authorisation.authorisation()

    id_ = '2344f4b3-a7bd-4512-686d-08d8c4533103'

    r = gepgraphy.get_by_id(token, id_)

    assert r['metadata']['message'] == 'Object not found', 'Система не вернула ошибку Object not found'
