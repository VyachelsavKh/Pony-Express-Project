import request_authorisation
import event_71_requests
import log_output

'''
Тест-кейс №1. Проверка получения конфигурации бэкэнда
1) Войти в систему - 
    бот зашёл в систему
2) Отправить запрос на получение конфигурации бэкэнда - 
    система вернула код успеха 200
'''

def request_8():
    log_output.Print('Тест 8')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 8 не пройден')
        return

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == 'ERROR':
        log_output.Print('Тест 8 не пройден')
        return

    if r['result']['id'] != None:
        log_output.Print('Блок успешно создан, его id: ' + r['result']['id'])
        log_output.Print('Тест 8 пройден')
    else:
        log_output.Print('Тест 8 не пройден')
        return

if __name__ == "__main__":
    request_8()