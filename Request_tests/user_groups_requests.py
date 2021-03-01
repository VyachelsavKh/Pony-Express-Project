import send_request
import json
import allure

def get_all_groups(token):
    url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/get-limit/1000'

    with allure.step('Отправил запрос на получение всех групп пользователей'):
        r = send_request.get_request(url, headers = {'Authorization': f'Bearer {token}'})
        
        return json.loads(r.text)

def create_group(token, name):
    url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/post-item'
    headers = { 'Authorization': f'Bearer {token}',
                'Content-Type':'application/json'}
    data = {'displayName':name}

    with allure.step('Отправил запрос на создание группы с именем: ' + name):
        r = send_request.post_request(url, json = data, headers = headers)

        return json.loads(r.text)

def delete_group(token, id):
    url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/delete-item'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'id': id}

    with allure.step('Отправил запрос на удаление группы с id: ' + id):
        r = send_request.delete_request(url, headers = headers, params = params)

        return json.loads(r.text)