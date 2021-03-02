import request_authorisation
import event_71
import pytest

'''
Тест-кейс №11. Проверка ввода некорректного номера накладной в блок событий 71
1) Войти в систему -
    бот зашёл в систему
2) Отправить запрос на создание блока событий 71 без курьера -
    Блок был создан
3) Отправить запрос на создание блока с номером "0012345666" -
    Система не вернула ошибку «Марка не привязана»
'''

def test_11():
    token = request_authorisation.authorisation()

    r = event_71.without_sorting_and_couriers(token)

    id_ = r['result']['id']

    assert id_ != None, 'Блок не был создан'

    number = "0012345666"

    r = event_71.add_object(token, id_, number)

    assert r['metadata']['message'] == "Марка не привязана", 'Система не вернула ошибку «Марка не привязана»'
