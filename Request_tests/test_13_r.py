import request_authorisation
import event_79
import paths_r
import pytest

'''
Тест-кейс №13. Создание блока событий 79
1) Войти в систему -
    бот зашёл в систему
2) Отправить запрос на создание блока событий с точкой назначения "1202" -
    Блок был создан
'''


def test_13():
    token = request_authorisation.authorisation()

    destinationPointId = paths_r.destinationPointId_1202

    r = event_79.included_in_consolidation(token, destinationPointId)

    destinationPoint = r['result']['destinationPoint']

    assert destinationPoint['code'] == '1202', 'Попал в другой блок'
