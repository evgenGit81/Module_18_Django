from django.shortcuts import render
from django.views.generic import TemplateView

class Platform(TemplateView):

    title = 'Магазинчик'
    main_head = "Добро пожаловать в магазин по покупке всего и ничего!"
    extra_context = {
        'main_head': main_head,
        'title': title,

    }
    template_name = 'third_task/index.html'

    # context = {
    #     'title': title,
    #     'main_head': main_head
    # }
    # def ret_cont(self, request):
    #     return render(request, 'third_task/index.html', self.context)

def catalog(request):
    return render(request, 'third_task/catalog.html')

def bag(request):
    return render(request, 'third_task/bag.html')
