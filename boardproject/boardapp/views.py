from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):

    # Modelデータ取得サンプル
    # my_object = User.objects.all()
    my_object = User.objects.get(username='tester')
    # print(my_object)
    print(my_object.email)

    if request.method == "POST":
        print("Hello")
    else:
        print("No")
    return render(request, 'signup.html', {'some': 100})