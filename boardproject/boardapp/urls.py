from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc,listfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('list/', listfunc, name='list')
]
