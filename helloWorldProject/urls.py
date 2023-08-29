from django.contrib import admin
from django.urls import path

# .viewsからインポートして呼び出す必要あり
from .views import sampleAction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', sampleAction)
]
