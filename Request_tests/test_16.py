import request_authorisation
import gepgraphy

'''
Тест-кейс №16 Тестирование отрицательной работы сервиса географии
1) Войти в систему -
    бот зашёл в систему
2) Отправить запрос на сервис на поиск адреса объекта по неправильному id -
    Система не вернула ошибку "Object not found"
'''

def test_16():
    token = request_authorisation.authorisation()

    id_ = '2344f4b3-a7bd-4512-686d-08d8c4533103'

    r = gepgraphy.get_by_id(token, id_)

    assert r['metadata']['message'] == 'Object not found', 'Система не вернула ошибку Object not found'
