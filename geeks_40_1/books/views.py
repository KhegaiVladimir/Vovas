from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Books
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


def books_view(request):
    if request.method == 'GET':
        books = Books.objects.filter().order_by('-id')
        return render(request, template_name='books.html', context={'books':books})

def books_details_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Books, id=id)
        return render(request, template_name='books_details.html', context={'book_id':book_id})