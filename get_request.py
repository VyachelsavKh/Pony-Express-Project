import requests
from paths import urls
import log_output

def get_request(token, num, api, params = None):
    if params is None:
        try:
            r = requests.get(urls[num] + api, headers={'Authorization': f'Bearer {token}'})
            if r.status_code != 200:
                log_output.Print('Запрос вернул код ошибки')
            else:
                log_output.Print('Запрос вернул код успеха')
        except:
            log_output.Print('Не смог отправить запрос')
            return 'ERROR'
    else:
        try:
            r = requests.get(urls[num] + api, headers={'Authorization': f'Bearer {token}'}, params=params)
            if r.status_code != 200:
                log_output.Print('Запрос вернул код ошибки')
            else:
                log_output.Print('Запрос вернул код успеха')
        except:
            log_output.Print('Не смог отправить запрос')
            return 'ERROR'
    return r