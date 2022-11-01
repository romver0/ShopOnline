from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views import View
from store.models.infoUser import InfoUser


class Signup(View):
    def post(self, request):
        print(f'request.POST = {request.POST}')
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']
        print(f'first_name = {first_name}\nlast_name={last_name}\npassword={password}\nphone={phone}\nemail={email}')

        user = InfoUser(
            first_name=first_name,
            last_name=last_name,
            password=password,
            phone=phone,
            email=email
        )
        error_message = self.error_checking(user)
        if not error_message:
            user.password = make_password(user.password)
            user.register()
            # login(request, user)
            return redirect('home')
        else:
            context = {
                'error': error_message,
                # 'skip': True
            }

        # return HttpResponse('Вы прошли регистрацию')
        return render(request, 'store/signupuser.html', context=context)

    def get(self, request):
        return render(request, 'store/signupuser.html',context={'skip': True})

    def error_checking(self, user):
        if not user.first_name:
            return 'Требуется имя!'
        if not user.last_name:
            return 'Требуется фамилия!'
        if not user.email:
            return 'Требуется емайл'
        if not user.password:
            return 'Требуется пароль'
        if len(user.password) < 6:
            return 'Короткий пароль'
        if not user.phone:
            return 'Требуется телефон'
        if user.isExists():
            return 'Такая почта уже существует'
