import request_authorisation
import event_71_requests
import log_output

'''

'''

def request_9():
    log_output.Print('Тест 9')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 9 не пройден')
        return

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == 'ERROR':
        log_output.Print('Тест 9 не пройден')
        return

    id_ = r['result']['id']

    if id_ != None:
        log_output.Print('Блок успешно создан, его id: ' + id_)
    else:
        log_output.Print('Тест 9 не пройден')
        return

    number = "11-1111-1111"

    r = event_71_requests.add_object(token, id_, number)

    if r == 'ERROR' or r['result'] == None:
        log_output.Print('Не смог добавить накладную с номером: ' + number)
        log_output.Print('Тест 9 не пройден')
        return

    waybill_id = r['result']['id']

    r = event_71_requests.find_object(token, id_)

    if r == 'ERROR' or r['result'] == None:
        log_output.Print('Не смог добавить найти добавленные накладные')
        log_output.Print('Тест 9 не пройден')
        return

    for waybill in r['result']:
        if waybill['id'] == waybill_id:
            log_output.Print('Добавил накладную с номером: ' + number + ' и id: ' + waybill_id)
            log_output.Print('Тест 9 пройден')
            return

    log_output.Print('Не смог найти накладную с номером: ' + number + ' и id: ' + waybill_id)
    log_output.Print('Тест 9 не пройден')
    return

if __name__ == "__main__":
    request_9()