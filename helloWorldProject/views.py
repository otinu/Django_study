from django.http import HttpResponse
from django.views.generic import TemplateView

def sampleAction(request):
    return ("<h3>Hello Django</h3>")

class sampleTemplateView(TemplateView):
    template_name = "hello.html"