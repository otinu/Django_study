from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError


def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            # この行が実行される時点でユーザー登録は完了する
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'signup.html', {'error_message': 'ユーザーは登録済みでした'})

        # この行で登録内容の更新などが実行される
        # user.save()

    '''
    Modelデータ取得サンプル

    # my_object = User.objects.all()
    my_object = User.objects.get(username='tester')
    # print(my_object)
    print(my_object.email)
    '''
    return render(request, 'signup.html', {'some': 100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'login_message': 'logged in'})
        else:
            return render(request, 'login.html', {'login_message': 'not logged in'})
    return render(request, 'login.html', {'login_message': 'get method'})