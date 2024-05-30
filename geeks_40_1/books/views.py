from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from . import forms
import datetime
from django.views import generic

time = datetime.datetime.now()

class NameView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Меня зовут Владимир, мне 16 лет')


class HobbyVIew(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Моё хобби это программирование')

# def hobby_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Моё хобби это программирование')

class TimeView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Нынешнее время: {time}')

# def time_view(request):
#     if request.method == 'GET':
#         return HttpResponse(f'Нынешнее время: {time}')


class BooksView(generic.ListView):
    template_name = 'books.html'
    context_object_name = 'books'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

# def books_view(request):
#     if request.method == 'GET':
#         books = Books.objects.filter().order_by('-id')
#         return render(request, template_name='books.html', context={'books':books})

class BooksDetailsView(generic.DetailView):
    template_name = 'books_details.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)




# def books_details_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(Books, id=id)
#         return render(request, template_name='books_details.html', context={'book_id':book_id})

class CreateReviewView(generic.CreateView):
    template_name = 'create_review.html'
    form_class = forms.ReviewForm
    success_url = '/'


    def from_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)




# def create_review_view(request, id):
#     if request.method == 'POST':
#         form = forms.ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Your review has been created</h1>')
#     else:
#         form = forms.ReviewForm()
#     return render(request, 'create_review.html', {'form': form, 'book_id': id})

class DeleteBooksView(generic.DeleteView):
    template_name = 'delete_books.html'
    success_url = '/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)

# def delete_books_view(request, id):
#     book = get_object_or_404(Books, id=id)
#     book.delete()
#     return HttpResponse('<h1>Your book has been deleted</h1>')


class CreateBookView(generic.CreateView):
    template_name = 'create_books.html'
    form_class = forms.BooksForm
    success_url = '/'

    def from_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)

# def create_books_view(request):
#     if request.method == 'POST':
#         form = forms.BooksForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Your book has been created</h1>')
#     else:
#         form = forms.BooksForm()
#         return render(request, 'create_books.html', {'form': form})


class EditBookView(generic.UpdateView):
    template_name = 'edit.html'
    form_class = forms.BooksForm
    success_url = '/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBookView, self).form_valid(form=form)


# def edit_books_view(request, id):
#     book_id = get_object_or_404(Books, id=id)
#     if request.method == 'POST':
#         form = forms.BooksForm(request.POST,instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Your book has been updated</h1>')
#     else:
#         form = forms.BooksForm(instance=book_id)
#     return render(request, 'edit.html', {'form': form, book_id: 'book_id' })

