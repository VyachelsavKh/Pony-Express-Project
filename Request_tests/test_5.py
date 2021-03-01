import request_authorisation
import user_groups_requests
import pytest

'''
Тест-кейс №5. Просмотр списка групп пользователей
1) Войти в систему - 
    бот зашёл в систему
2) Отправить запрос на получение всех групп пользователей - 
    бот вернул все группы пользователей
'''

def test_5():
    token = request_authorisation.authorisation()

    r = user_groups_requests.get_all_groups(token)

    assert r['result'] != None, 'Не смог найти группы'