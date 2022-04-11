import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # workdir = ', '.join(os.listdir())
    template_name = 'app/dir.html'
    table = dict()

    workdir = os.listdir()

    for _ in workdir:
        dir_name = os.path.join(os.getcwd(), _)
        size = f'{os.path.getsize(dir_name)} bytes'
        time = datetime.fromtimestamp(os.path.getmtime(dir_name)).strftime('%d-%m-%Y %H:%M:%S')


        if os.path.isfile(dir_name):
            type_ = 'Файл'
        elif os.path.isdir(dir_name):
            type_ = 'Папка'
        else:
            type_ = 'Не определено'

        table[_] = [type_, size, time]

    # msg = f'Рабочий каталог:\n{workdir}'

    context = {
        'table': table
    }
    return render(request, template_name, context)
