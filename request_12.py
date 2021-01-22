import request_authorisation
import event_71_requests
import log_output

'''

'''

def request_12():
    log_output.Print('Тест 12')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 12 не пройден')
        return

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == 'ERROR':
        log_output.Print('Тест 12 не пройден')
        return

    id_ = r['result']['id']

    if id_ != None:
        log_output.Print('Блок успешно создан, его id: ' + id_)
    else:
        log_output.Print('Тест 12 не пройден')
        return

    number = "11-1111-1111"

    r = event_71_requests.add_object(token, id_, number)

    if r == 'ERROR' or r['result'] == None:
        log_output.Print('Не смог добавить накладную с номером: ' + number)
        log_output.Print('Тест 12 не пройден')
        return

    waybill_id = r['result']['id']

    r = event_71_requests.find_object(token, id_)

    if r == 'ERROR' or r['result'] == None:
        log_output.Print('Не смог добавить найти добавленные накладные')
        log_output.Print('Тест 12 не пройден')
        return

    find = 0

    for waybill in r['result']:
        if waybill['id'] == waybill_id:
            find = 1
            break

    if find:
        log_output.Print('Добавил накладную с номером: ' + number + ' и id: ' + waybill_id)
    else:
        log_output.Print('Не смог найти накладную с номером: ' + number + ' и id: ' + waybill_id)
        log_output.Print('Тест 12 не пройден')
        return

    r = event_71_requests.delete_object(token, waybill_id)

    if r == 'ERROR':
        log_output.Print('Тест 12 не пройден')
        return

    r = event_71_requests.find_object(token, id_)

    if r == 'ERROR' or r['result'] == None:
        log_output.Print('Не смог добавить найти добавленные накладные')
        log_output.Print('Тест 12 не пройден')
        return

    find = 0

    for waybill in r['result']:
        if waybill['id'] == waybill_id:
            find = 1
            break

    if find:
        log_output.Print('Накладная с номером: ' + number + ' и id: ' + waybill_id + ' не была удалена')
        log_output.Print('Тест 12 не пройден')
        return
    else:
        log_output.Print('Накладная с номером: ' + number + ' и id: ' + waybill_id + ' была удалена')
        log_output.Print('Тест 12 пройден')
        return

if __name__ == "__main__":
    request_12()