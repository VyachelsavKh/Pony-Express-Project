import request_authorisation
import log_output
import warehouse_requests
from condition_parametrs import codes as right_codes

'''
Тест-кейс №4. Проверка получения всех параметров состояний у склада
1) Войти в систему - 
    бот зашёл в систуме
2) Отправить поисковый запрос на получение всех параметров состояний - 
    система вернула код успеха 200
3) Сравнить их количество с ожидаемым - 
    они совпадают
4) Сравнить параметры состояний с ожидаемыми - 
    они не отличаются
'''

def request_4():
    log_output.Print('Тест 4')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 4 не пройден')
        return

    log_output.Print('Отправил запрос на получение всех параметров сотояний')

    r4 = warehouse_requests.get_condition_parameters(token)

    if r4 == 'ERROR':
        log_output.Print('Тест 4 не пройден')
        return

    code_list = r4['result']

    now_codes = []

    for code in code_list:
        now_codes.append([code['code'], code['name']])

    if len(now_codes) != len(right_codes):
        log_output.Print('Количество параметров состойний отличается от ожидаемого')
        log_output.Print('Тест 4 не пройден')
        return

    log_output.Print('Количество параметров состойний не отличается от ожидаемого')

    for code in now_codes:
        if not code in right_codes:
            log_output.Print('Параметры состойний отличаются от ожидаемого')
            log_output.Print('Тест 4 не пройден')
            return

    log_output.Print('Параметры состойний не отличаются от ожидаемого')

    log_output.Print('Тест 4 пройден')

if __name__ == "__main__":
    request_4()