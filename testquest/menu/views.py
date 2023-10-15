from django.http import HttpResponseNotFound
from django.shortcuts import render

actual_menu_name = ""
actual_menu_items = []

def index(request):
    return render(request, 'menu/index.html')

def openmenu(request, menu_name):
    return categories(request, actual_menu_name, '')

def categories(request, menu_name, categorypath):
    return render(request, 'menu/menu.html', {'title': menu_name})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')

def inBase(path):
    return True