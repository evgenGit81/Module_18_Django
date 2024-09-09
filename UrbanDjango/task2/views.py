from django.shortcuts import render
from django.views.generic import TemplateView

class class_templ(TemplateView):
    template_name = 'class_template.html'

def func_templ(request):
    return render(request, 'func_template.html')
