import requests
import json
import log_output

def included_in_consolidation(token, destinationPointId):
    url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/event-blocks79/post-item'
    headers = {'Authorization': f'Bearer {token}'}
    data = {"description":"","destinationPointId":destinationPointId}

    log_output.Print('Отправил запрос на создание блока событий - 79 включён в консолидацию')

    r = requests.post(url, json=data, headers=headers)

    if r.status_code != 200:
        log_output.Print('Запрос вернул код ошибки')
        return 'ERROR'
    else:
        log_output.Print('Запрос вернул код успеха')

    return json.loads(r.text)

def add_object(token, id_, number):
    url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events79/post-item'
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        "IsRouteValidationEnabled": False,
        "eventBlockId": id_,
        "pointId": "07c5c96a-6f52-428d-9332-0004c296067e",
        "scannedNumber": number,
        "hostname": "DESKTOP-M4BHSDU"
    }

    log_output.Print('Отправил запрос на добавления объекта с номером: ' + number)

    r = requests.post(url, json = data, headers = headers)

    if r.status_code != 200:
        log_output.Print('Запрос вернул код ошибки')
        return 'ERROR'
    else:
        log_output.Print('Запрос вернул код успеха')

    return json.loads(r.text)