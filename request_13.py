import request_authorisation
import event_79_requests
import log_output
import paths

'''

'''


def request_13():
    log_output.Print('Тест 13')

    token = request_authorisation.authorisation()

    if token == 'ERROR':
        log_output.Print('Тест 13 не пройден')
        return

    destinationPointId = paths.destinationPointId_1202

    r = event_79_requests.included_in_consolidation(token, destinationPointId)

    if r == 'ERROR':
        log_output.Print('Тест 13 не пройден')
        return

    destinationPoint = r['result']['destinationPoint']

    if destinationPoint['code'] == '1202':
        log_output.Print('Блок успешно создан')
        log_output.Print('Тест 13 пройден')
        return
    else:
        log_output.Print('Попал в другой блок')
        log_output.Print('Тест 13 не пройден')
        return

if __name__ == "__main__":
    request_13()