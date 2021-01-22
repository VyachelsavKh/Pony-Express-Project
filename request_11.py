import request_authorisation
import event_71_requests
import log_output

'''

'''

def request_11():
    log_output.Print('Тест 11')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 11 не пройден')
        return

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == 'ERROR':
        log_output.Print('Тест 11 не пройден')
        return

    id_ = r['result']['id']

    if id_ != None:
        log_output.Print('Блок успешно создан, его id: ' + id_)
    else:
        log_output.Print('Тест 11 не пройден')
        return

    number = "0012345666"

    r = event_71_requests.add_object(token, id_, number)

    if r == 'ERROR':
        log_output.Print('Не смог вбить номер марки: ' + number)
        log_output.Print('Тест 11 не пройден')
        return

    if r['metadata']['message'] == "$_MARK_IS_NOT_BOUND_$":
        log_output.Print('Система вернула ошибку «Марка не привязана»')
        log_output.Print('Тест 11 пройден')
        return
    else:
        log_output.Print('Система добавила добавила марку с номером: ' + number)
        log_output.Print('Тест 11 не пройден')
        return

if __name__ == "__main__":
    request_11()