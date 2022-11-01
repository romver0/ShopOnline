from django.shortcuts import HttpResponse, redirect


class FirstMiddleware:
    def __init__(self, get_response):
        print('сработал middleware')
        self._get_response = get_response
        self.name = 'middleware'
        self.age = 0

    def __call__(self, request):
        response = self._get_response(request)
        # print(f"request.session.keys={request.session.keys()}")
        # print(f"request.session.get('category')={request.session.get('category')}")
        return response

    def process_exception(self, request, exception):
        print(f'exception = {exception}')
        return HttpResponse('Миддливаре нашёл ошибку!!!')


