import requests

def get_request(url, headers, params = None):
    try:
        r = requests.get(url, headers = headers, params = params)
        assert r.status_code == 200, 'Запрос вернул код ошибки'
    except:
        assert 0, 'Не смог отправить запрос'
    return r

def post_request(url, headers, data = None, json = None):
    try:
        r = requests.post(url, headers = headers, data = data, json = json)
        assert r.status_code == 200, 'Запрос вернул код ошибки'
    except:
        assert 0, 'Не смог отправить запрос'
    return r

def delete_request(url, headers, params = None):
    try:
        r = requests.delete(url, headers = headers, params = params)
        assert r.status_code == 200, 'Запрос вернул код ошибки'
    except:
        assert 0, 'Не смог отправить запрос'
    return r