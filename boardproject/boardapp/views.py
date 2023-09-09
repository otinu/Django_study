from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import BoardModel



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

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')