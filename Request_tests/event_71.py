import json
import allure
import send_request

def without_sorting_and_couriers(token):
    url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/event-blocks71/post-item'
    headers = {'Authorization': f'Bearer {token}'}
    data = {"description" : ""}

    with allure.step('Создание блока событий-71 прибыл на склад без сортировки без курьера'):
        r = send_request.post_request(url, json = data, headers = headers)

        return json.loads(r.text)

def add_object(token, id_, number):
    url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/post-item'
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        "eventBlockId" : id_,
        "pointId" : "07c5c96a-6f52-428d-9332-0004c296067e",
        "scannedNumber" : number,
        "hostname" : "DESKTOP-M4BHSDU"
    }

    with allure.step('Добавления объекта с номером: ' + number):
        r = send_request.post_request(url, json = data, headers = headers)

        return json.loads(r.text)

def find_object(token, id_):
    url = f'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/get-events-by-event-block-id/{id_}'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'id' : id_}

    with allure.step('Поиск объекта с id: ' + id_):
        r = send_request.get_request(url, headers = headers, params = data)

        return json.loads(r.text)

def delete_object(token, id_):
    url = f'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/delete-item/{id_}'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'id': id_}

    with allure.step('Удаление объекта с id: ' + id_):
        r = send_request.delete_request(url, headers = headers, params = data)

        return json.loads(r.text)