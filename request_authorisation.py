import requests
import json
import paths
import log_output

def authorisation():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'username': paths.correct_enter_login,
              'password': paths.correct_enter_password,
              'grant_type': 'password',
              'scope': 'pegasus',
              'client_id': 'pegasus-v2',
              'client_secret': 'secret'}

    url = "http://srv-pnew-02-test:1001/auth/connect/token"

    try:
        r = requests.post(url, data = data, headers = headers)
    except:
        log_output.Print('Не зашёл в систему')
        return 'ERROR'

    log_output.Print('Вошёл в систему')

    answer = json.loads(r.text)
    return(answer["access_token"])

if __name__ == "__main__":
    token = authorisation()