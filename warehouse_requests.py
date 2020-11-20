import get_request
import json
import log_output

def get_condition_parameters(token):
    r = get_request.get_request(token, 12, '/api/v1/condition-parameters/get-all')

    if r == 'ERROR':
        return 'ERROR'

    r = json.loads(r.text)

    return r

def print_condition_parameters(token):
    r4 = get_condition_parameters(token)

    code_list = r4['result']

    out = 'codes = [\n'

    for code in code_list:
        out += '[' + str(code['code']) + ', ' + "'" + code['name'] + "'" + '],\n'

    out += ']'

    print(out)

