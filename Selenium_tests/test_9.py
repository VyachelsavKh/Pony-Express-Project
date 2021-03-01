import request_authorisation
import event_71
import pytest

'''
Тест-кейс №9. Проверка ввода некорректного номера накладной в блок событий 71
1) Войти в систему -
    бот зашёл в систему
2) Отправить запрос на создание блока событий 71 без курьера -
    Блок был создан
3) Отправить запрос на добавление накладной с номером "11-1111-1111" -
    накладная с номером "11-1111-1111" добавилась
'''

def test_9():
    token = request_authorisation.authorisation()

    r = event_71.without_sorting_and_couriers(token)

    id_ = r['result']['id']

    assert id_ != None, 'Блок не был создан'

    number = "11-1111-1111"

    r = event_71.add_object(token, id_, number)

    assert r['result'] != None, 'Не смог добавить накладную'

    waybill_id = r['result']['id']

    r = event_71.find_object(token, id_)

    assert r['result'] != None, 'Не смог добавить найти добавленные накладные'

    for waybill in r['result']:
        if waybill['id'] == waybill_id:
            return

    assert 0, 'Не смог найти созданную накладную'
