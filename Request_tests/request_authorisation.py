import json
import paths
import send_request
import requests
import allure

def authorisation(wrong = False):
    login = paths.correct_enter_login
    password = paths.correct_enter_password

    if wrong:
        login = paths.wrong_enter_login
        password = paths.wrong_enter_password

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'username': login,
            'password': password,
            'grant_type': 'password',
            'scope': 'pegasus',
            'client_id': 'pegasus-v2',
            'client_secret': 'secret'}

    url = "http://srv-pnew-02-test:1001/auth/connect/token"

    if not wrong:
        with allure.step('Вход в систему'):

            r = send_request.post_request(url, headers = headers, data = data)

            answer = json.loads(r.text)

            return answer["access_token"]
    else:
        return requests.post(url, headers = headers, data = data)