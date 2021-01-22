import request_authorisation
import log_output
import user_groups_requests
import datetime

'''
Тест-кейс №5. Проверка права на создание группы пользователей и удаление её
1) Войти в систему - 
    бот зашёл в систему
2) Отправить запрос на получение всех групп пользователей - 
    бот вернул все группы пользователей
3) Отправить запрос на создание группы - 
    система вернула код успеха 200
4) Отправить запрос на получение всех групп пользователей - 
    бот вернул все группы пользователей
5) Искать среди групп пользователей новую созданную группу - 
    группа нашлась
6) Отправить запрос на удаление созданной группы - 
    система вернула код успеха 200
7) Отправить запрос на получение всех групп пользователей - 
    бот вернул все группы пользователей
8) Искать среди групп пользователей новую созданную группу - 
    группа не нашлась
'''

def request_5():
    log_output.Print('Тест 5')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 5 не пройден')
        return

    r = user_groups_requests.get_all_groups(token)

    if r == 'ERROR':
        log_output.Print('Тест 5 не пройден')
        return

    if r['result'] == None:
        log_output.Print('Не смог найти группы')
        log_output.Print('Тест 5 не пройден')
        return

    log_output.Print('Получил все группы пользователей')

    date = datetime.datetime.now()
    name = date.strftime('%Y.%d.%m,%H.%M.%S.test_groop_request')

    for group in r['result']:
        if group['displayName'] == name:
            log_output.Print('Группа с именем: ' + name + ' уже существует')
            log_output.Print('Тест 5 не пройден')
            return

    r = user_groups_requests.create_group(token, name)

    if r['result'] == None:
        log_output.Print('Не смог создать группу')
        log_output.Print('Тест 5 не пройден')
        return

    id = r['result']['id']

    r = user_groups_requests.get_all_groups(token)

    if r == 'ERROR':
        log_output.Print('Тест 5 не пройден')
        return

    if r['result'] == None:
        log_output.Print('Не смог найти группы')
        log_output.Print('Тест 5 не пройден')
        return

    exists = 0

    for group in r['result']:
        if group['displayName'] == name and group['id'] == id:
            exists = 1

    if not exists:
        log_output.Print('Не нашёл созданную группу')
        log_output.Print('Тест 5 не пройден')
        return

    log_output.Print('Нашёл созданную группу с именем: ' + name + ' и id: ' + id)

    r = user_groups_requests.delete_group(token, id)

    if r == 'ERROR':
        log_output.Print('Тест 5 не пройден')
        return

    r = user_groups_requests.get_all_groups(token)

    if r == 'ERROR':
        log_output.Print('Тест 5 не пройден')
        return

    if r['result'] == None:
        log_output.Print('Не смог найти группы')
        log_output.Print('Тест 5 не пройден')
        return

    exists = 0

    for group in r['result']:
        if group['displayName'] == name and group['id'] == id:
            exists = 1

    if exists:
        log_output.Print('Группа не удалилась')
        log_output.Print('Тест 5 не пройден')
        return

    log_output.Print('Группа удалилась')

    log_output.Print('Тест 5 пройден')

if __name__ == "__main__":
    request_5()