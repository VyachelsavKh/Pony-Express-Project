import requests
import json
import log_output

def without_sorting_and_couriers(token):
    url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/event-blocks71/post-item'
    headers = {'Authorization': f'Bearer {token}'}
    data = {"description" : ""}

    log_output.Print('Отправил запрос на создание блока событий-71 прибыл на склад без сортировки без курьера')

    r = requests.post(url, json = data, headers = headers)

    if r.status_code != 200:
        log_output.Print('Запрос вернул код ошибки')
        return 'ERROR'
    else:
        log_output.Print('Запрос вернул код успеха')

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

    log_output.Print('Отправил запрос на добавления объекта с номером: ' + number)

    r = requests.post(url, json = data, headers = headers)

    if r.status_code != 200:
        log_output.Print('Запрос вернул код ошибки')
        return 'ERROR'
    else:
        log_output.Print('Запрос вернул код успеха')

    return json.loads(r.text)

def find_object(token, id_):
    url = f'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/get-events-by-event-block-id/{id_}'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'id' : id_}

    log_output.Print('Отправил запрос на поиск объекта с id: ' + id_)

    r = requests.get(url, headers = headers, params = data)

    if r.status_code != 200:
        log_output.Print('Запрос вернул код ошибки')
        return 'ERROR'
    else:
        log_output.Print('Запрос вернул код успеха')

    return json.loads(r.text)

def delete_object(token, id_):
    url = f'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events71/delete-item/{id_}'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'id': id_}

    log_output.Print('Отправил запрос на удаление объекта с id: ' + id_)

    r = requests.delete(url, headers = headers, params = data)

    if r.status_code != 200:
        log_output.Print('Запрос вернул код ошибки')
        return 'ERROR'
    else:
        log_output.Print('Запрос вернул код успеха')

    return json.loads(r.text)