import request_authorisation
import event_79_requests
import log_output
import paths

'''

'''


def request_14():
    log_output.Print('Тест 14')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 14 не пройден')
        return

    destinationPointId = paths.destinationPointId_1202

    r = event_79_requests.included_in_consolidation(token, destinationPointId)

    if r == 'ERROR' or r['result'] == None:
        log_output.Print('Не смог создать блок событий 79 - включён в консолидацию')
        log_output.Print('Тест 14 не пройден')
        return

    destinationPoint = r['result']['destinationPoint']

    if destinationPoint['code'] != '1202':
        log_output.Print('Попал в другой блок')
        log_output.Print('Тест 14 не пройден')
        return

    log_output.Print('Блок успешно создан')

    id_ = r['result']['id']

    number = "99-9999-9999/999"

    r = event_79_requests.add_object(token, id_, number)

    if r == 'ERROR':
        log_output.Print('Не смог вбить номер места накладной')
        log_output.Print('Тест 14 не пройден')
        return

    if r['metadata']['message'] == "$_PLACE_IS_OUT_OF_RANGE_$":
        log_output.Print('Система вернула ошибку «Отсутствует введенное место накладной»')
        log_output.Print('Тест 14 пройден')
        return
    else:
        log_output.Print('Система нашла номер места накладной: ' + number)
        log_output.Print('Тест 14 не пройден')
        return

if __name__ == "__main__":
    request_14()