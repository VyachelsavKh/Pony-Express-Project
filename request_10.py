import request_authorisation
import event_71_requests
import log_output

'''

'''

def request_10():
    log_output.Print('Тест 10')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 10 не пройден')
        return

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == 'ERROR':
        log_output.Print('Тест 10 не пройден')
        return

    id_ = r['result']['id']

    if id_ != None:
        log_output.Print('Блок успешно создан, его id: ' + id_)
    else:
        log_output.Print('Тест 10 не пройден')
        return

    number = "11-1111-1112"

    r = event_71_requests.add_object(token, id_, number)

    if r == 'ERROR':
        log_output.Print('Не смог вбить номер накладной: ' + number)
        log_output.Print('Тест 10 не пройден')
        return

    if r['metadata']['message'] == "$_OBJECT_NUMBER_NOT_VALID_$: 11-1111-1112":
        log_output.Print('Система вернула ошибку «Номер объекта не валидный»')
        log_output.Print('Тест 10 пройден')
        return
    else:
        log_output.Print('Система добавила накладную с номером: ' + number)
        log_output.Print('Тест 10 не пройден')
        return

if __name__ == "__main__":
    request_10()