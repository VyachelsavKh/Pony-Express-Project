import request_authorisation
import gepgraphy

'''
Тест-кейс №17 Тестирование отрицательной работы сервиса географии
1) Войти в систему -
    бот зашёл в систему
2) Отправить запрос на получение полигона адреса по неправильному id
    Система вернула ошибку $_ADDRESS_NOT_FOUND_$
'''

def test_17():
    token = request_authorisation.authorisation()

    id_ = '2344f4b3-a7bd-4512-686d-08d8c4533103'

    r = gepgraphy.get_polygon_by_address_id(token, id_)

    assert '$_ADDRESS_NOT_FOUND_$' in r['metadata']['message'], 'Система не вернула ошибку $_ADDRESS_NOT_FOUND_$'
