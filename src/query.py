def query(request):

    if request == '':
        request = '{' + request + '}'
        return request

    if request[0] != '{':
        request = '{' + request

    if request[-1] != '}':
        request = request + '}'

    return request
