from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.infoUser import InfoUser


class Login(View):
    returnURL=None
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = InfoUser.get_infoUser_by_email(email=email)

        error_message=None
        if not user:
            context = {
                # 'error': 'С такими данными пользователя не существует',
                'error': 'С такой почтой нет пользователя',
                # 'skip': True
            }
            return render(request, 'store/../../templates/registration/login.html', context=context)
        else:
            # login(request, user)
            # password = check_password(password)
            # return redirect('home')
            is_password = check_password(password, user.password)
            if is_password:
                request.session['user_id'] = user.id
                # request.session['hren'] = 'loremloremlorem'
                # print(request.session.keys())
                # print(request.session['hren'])
                if Login.returnURL:
                    pass
                else:
                    Login.returnURL=None
                    return redirect('home')
            else:
                error_message = 'Неправильно введён пароль'
            context = {
                'error': error_message,
                # 'skip': True,
            }
            return render(request, 'store/../../templates/registration/login.html', context=context)
            # return HttpResponse(f'Твой профиль {user.first_name} {user.last_name}')

    def get(self, request):
        print(request)
        context = {
            # 'skip': True
        }
        return render(request, 'store/../../templates/registration/login.html', context=context)


def logout(request):
    print(f'Сработал logout() request.session={request.session}')
    request.session.clear()
    return redirect('login')
