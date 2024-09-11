from django.shortcuts import render
from django.views.generic import TemplateView

class Platform(TemplateView):

    title = 'Магазинчик'
    main_head = "Добро пожаловать в магазин по покупке всего и ничего!"

    extra_context = {
        'main_head': main_head,
        'title': title,
        }
    template_name = 'fourth_task/index.html'


def catalog(request):
    main_head = "Вы в каталоге. Выбирайте что хотите!"
    cat = ['Танк', 'Танкер', 'Самолет', 'Дерижабль', 'Авианосец']
    len_cat = len(cat)
    context = {
            'cat': cat,
            'len_cat': len_cat,
            'main_head': main_head
            }
    return render(request, 'fourth_task/catalog.html', context)


def bag(request):
    title = "корзина"
    main_head = "Корзина."
    text = "К сожалению ваша сумочка слишком мала, чтобы унести в ней такое изделие! :( Возьмите, пожалуйста, сумку побольше."
    context = {
        "title": title,
        "main_head": main_head,
        "text": text,
    }
    return render(request, 'fourth_task/bag.html', context)

def fmenu(request):
    return render(request, 'fourth_task/menu.html')

