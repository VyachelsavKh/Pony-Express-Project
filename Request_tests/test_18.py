import request_authorisation
import gepgraphy

'''

'''

def test_18():
    token = request_authorisation.authorisation()

    id_ = '2344f4b3-a7bd-4512-686d-08d8c4533103'
    number = '11-1111-1111'

    r = gepgraphy.get_polygon_with_coordinates_by_address_id(token, id_, number)

    assert '$_ADDRESS_NOT_FOUND_$' in r['metadata']['message'], 'Система не вернула ошибку $_ADDRESS_NOT_FOUND_$'
