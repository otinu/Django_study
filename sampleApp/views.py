from django.shortcuts import render
from django.http import HttpResponse

def sampleAppView(request):
    return HttpResponse('app running!')
