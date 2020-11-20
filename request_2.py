import request_authorisation
import couriers_requests
import log_output

'''
Тест-кейс №2. Проверка получения конфигурации бэкэнда
1) Войти в систему - 
    бот зашёл в систуме
2) Отправить запрос на получение курьера по id - 
    система вернула код успеха 200
3) Сравнить имя и фамилию курьера - 
    имя и фамилия курьера совпадают с ожидаемыми
'''

def request_2():
    log_output.Print('Тест 2')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 2 не пройден')

    r2 = couriers_requests.get_courier_by_id(token, '359afb0c-b870-4610-9233-524db1d5a029')

    if r2 == 'ERROR':
        log_output.Print('Тест 2 не пройден')
        return

    if r2['result']['firstName'] != 'Евгений ' or r2['result']['lastName'] != '(СТД) Бурлаченко':
        print('Это не тот курьер')
        log_output.Print('Тест 2 не пройден')
    else:
        print('Это нужный курьер')
        log_output.Print('Тест 2 пройден')

if __name__ == "__main__":
    request_2()