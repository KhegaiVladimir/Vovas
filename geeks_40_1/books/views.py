from django.shortcuts import render
from django.http import HttpResponse
import datetime

time = datetime.datetime.now()

def name_view(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Владимир, мне 16 лет')

def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('Моё хобби это программирование')

def time_view(request):
    if request.method == 'GET':
        return HttpResponse(f'Нынешнее время: {time}')
