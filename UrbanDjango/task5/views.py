from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ["Alex", "Evgeniy", "Nikita"]
info = {}


# def sign_up_by_html(request):
#     """html представление"""
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         repeat_password = request.POST.get("repeat_password")
#         age = int(request.POST.get("age"))
#
#         if username in users:
#             return HttpResponse("Пользователь с таким именем уже существует")
#         elif password != repeat_password:
#
#             return HttpResponse("Пароли не совпадают!")
#
#         elif age < 18:
#             return HttpResponse("Вы должны быть старше 18 лет!")
#         else:
#             return HttpResponse(f"Приветствуем, {username}!")
#     return render(request, "fifth_task/registration_page.html", context=info)

def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.username = form.cleaned_data['username']
            form.password = form.cleaned_data['password']
            form.repeat_password = form.cleaned_data['repeat_password']
            form.age = form.cleaned_data['age']
            if form.username in users:
                return HttpResponse("Пользователь с таким именем уже существует")
            elif form.password != form.repeat_password:
                return HttpResponse("Пароли не совпадают!")
            elif int(form.age) < 18:
                return HttpResponse("Вы должны быть старше 18 лет!")
            return HttpResponse(f"Приветствуем, {form.username}!")
        else:

            form = UserRegister()
            context = {
                'form': form,
            }
    return render(request, "fifth_task/registration_page.html", {'form': form})