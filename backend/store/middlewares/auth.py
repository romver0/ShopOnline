from django.shortcuts import redirect


def auth_middleware(get_response):
    print('вызов authentication_middleware')

    def middleware(request):
        print('вызов middleware')
        returnURL = request.META['PATH_INFO']
        print(f'returnURL={returnURL}')
        if not request.session['user_id']:
            return redirect(f'login?return_url={returnURL}')

        responce = get_response(request)
        print(f'responce= {responce}')
        return responce
    return middleware
