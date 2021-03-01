import json
import allure
import send_request

def get_by_id(token, id_):
    url = f'http://geography-backend-edu.pegasus.ponyex.local//api/v1/addresses/get-by-id/{id_}'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'id': id_}

    with allure.step('Поиск адреса объекта по id объекта'):
        r = send_request.get_request(url, headers=headers, params=data)

        return json.loads(r.text)

def get_polygon_by_address_id(token, id_):
    url = f'http://geography-backend-edu.pegasus.ponyex.local/api/v1/geography/get-polygon-by-address-id/{id_}'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'id': id_}

    with allure.step('Поиск полигона адреса объекта по id объекта'):
        r = send_request.get_request(url, headers=headers, params=data)

        return json.loads(r.text)

def get_polygon_with_coordinates_by_address_id(token, id_, number):
    url = f'http://geography-backend-edu.pegasus.ponyex.local/api/v1/geography/get-polygon-with-coordinates-by-address-id/{id_}?waybillNumber={number}'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'id': id_,
            'waybillNumber' : number}

    with allure.step('Поиск координат полигона адреса объекта по id объекта'):
        r = send_request.get_request(url, headers=headers, params=data)

        return json.loads(r.text)