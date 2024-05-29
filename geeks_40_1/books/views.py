from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Books
from . import forms
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


def create_review_view(request, id):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Your review has been created</h1>')
    else:
        form = forms.ReviewForm()
    return render(request, 'create_review.html', {'form': form, 'book_id': id})

def delete_books_view(request, id):
    book = get_object_or_404(Books, id=id)
    book.delete()
    return HttpResponse('<h1>Your book has been deleted</h1>')


def create_books_view(request):
    if request.method == 'POST':
        form = forms.BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Your book has been created</h1>')
    else:
        form = forms.BooksForm()
        return render(request, 'create_books.html', {'form': form})


def edit_books_view(request, id):
    book_id = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        form = forms.BooksForm(request.POST,instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Your book has been updated</h1>')
    else:
        form = forms.BooksForm(instance=book_id)
    return render(request, 'edit.html', {'form': form, book_id: 'book_id' })

