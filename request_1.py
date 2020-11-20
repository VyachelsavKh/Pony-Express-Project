import request_authorisation
import get_request
import log_output

'''
Тест-кейс №1. Проверка получения конфигурации бэкэнда
1) Войти в систему - 
    бот зашёл в систуме
2) Отправить запрос на получение конфигурации бэкэнда - 
    система вернула код успеха 200
'''

def request_1():
    log_output.Print('Тест 1')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 1 не пройден')

    log_output.Print('Отправил запрос на получение конфигурации бэкэнда')

    r1 = get_request.get_request(token, 0, '/api/v1/configurations/get-all')

    if r1 == 'ERROR' or r1.status_code != 200:
        log_output.Print('Тест 1 не пройден')
    else:
        log_output.Print('Тест 1  пройден')

if __name__ == "__main__":
    request_1()