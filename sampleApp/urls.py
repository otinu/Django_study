from django.urls import path
from .views import sampleAppView

urlpatterns = [
    path('sampleapp/', sampleAppView)
]
