import get_request
import json
import log_output

def get_courier_by_id(token, courier_id):
    log_output.Print('Ищу курьера с id = ' + courier_id)

    r = get_request.get_request(token, 1, f'/api/v1/couriers/get-courier-by-id/ {courier_id}', {'id': courier_id})

    if r == 'ERROR':
        return 'ERROR'

    r = json.loads(r.text)

    if r['result'] == None:
        log_output.Print('Не смог найти курьера с таким id')
        return 'ERROR'

    return r

def get_couriers(token, page_index, page_size, sort_direction=0, search=''):
    r = get_request.get_request(token, 1, '/api/v1/couriers/get-couriers',
                    {'PageIndex': page_index, 'PageSize': page_size, 'SortDirection': sort_direction, 'Search': search})

    if r == 'ERROR':
        return 'ERROR'

    r = json.loads(r.text)

    return r
