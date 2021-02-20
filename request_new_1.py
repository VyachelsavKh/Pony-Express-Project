import log_output
import request_authorisation
import requests
import json

def request_1():
    log_output.Print('Тест 1')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 1 не пройден')
        return

    id_ = '2344f4b3-a7bd-4512-686d-08d8c4533103'

    url = f'http://geography-backend-edu.pegasus.ponyex.local//api/v1/addresses/get-by-id/{id_}'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'id': id_}

    log_output.Print('Отправил запрос на поиск объекта с id: ' + id_)

    r = requests.get(url, headers=headers, params=data)

    if r.status_code != 200:
        log_output.Print('Запрос вернул код ошибки')
        return 'ERROR'
    else:
        log_output.Print('Запрос вернул код успеха')

    r = json.loads(r.text)

    if r['metadata']['message'] == 'Object not found':
        print('Объект не найден')
        print('Тест 1 пройден')
    else:
        print('Объект смог найтись')
        print('Тест 1 не пройден')


if __name__ == "__main__":
    request_1()