import request_authorisation
import couriers_requests
import log_output

'''
Тест-кейс №3. Проверка получения 5 курьеров с именем Максим
1) Войти в систему - 
    бот зашёл в систуме
2) Отправить поисковый запрос на поиск курьера с параметром Максим- 
    система вернула код успеха 200
3) Сравнить количество курьеров с таким параметром - 
    их 5
4) Сравнить их имена с Максим - 
    у каждого курьера имя Максим
'''

def request_3():
    log_output.Print('Тест 3')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 3 не пройден')

    log_output.Print('Отправил запрос на поиск 5 курьеров с параметром Максим')

    r3 = couriers_requests.get_couriers(token, 1, 5, 0, 'Максим')

    if r3 == 'ERROR':
        log_output.Print('Тест 3 не пройден')

    if r3['result']['count'] != 5:
        log_output.Print('Не нашёл 5 курьеров у которых один из параметров равен Максим')
        log_output.Print('Тест 3 не пройден')
        return

    log_output.Print('Нашёл 5 курьеров у которых один из параметров равен Максим')
    couriers_list = r3['result']['items']

    for courier in couriers_list:
        if courier['firstName'] != 'Максим':
            log_output.Print('Имя курьера не Максим')
            log_output.Print('Тест 3 не пройден')
            return

    log_output.Print('У каждого курьера имя Максим')
    log_output.Print('Тест 3 пройден')

if __name__ == "__main__":
    request_3()