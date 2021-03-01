import request_authorisation
import event_71
import pytest

'''
Тест-кейс №8. Создание блока событий 71 без курьера
1) Войти в систему -
    бот зашёл в систему
2) Отправить запрос на создание блока событий 71 без курьера -
    Блок был создан
'''

def test_8():
    token = request_authorisation.authorisation()

    r = event_71.without_sorting_and_couriers(token)

    assert r['result']['id'] != None, 'Блок не был создан'
