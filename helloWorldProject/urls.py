from django.contrib import admin
from django.urls import path, include

# .viewsからインポートして呼び出す必要あり
from .views import sampleAction, sampleTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', sampleAction),
    path('helloworld/', sampleTemplateView.as_view()),
    # include()を使って、app内のurls.pyに橋渡し
    path('', include('sampleApp.urls'))
]
