import request_authorisation
import gepgraphy

'''

'''

def test_19():
    token = request_authorisation.authorisation()

    id_ = 'ad9204fb-4007-4185-9288-503e55f66f0c'

    r = gepgraphy.get_by_id(token, id_)

    assert r['result'] is not None, 'Система не нашла объект'
