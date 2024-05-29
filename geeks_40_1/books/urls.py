from django.urls import path
from .views import name_view, hobby_view, time_view, books_view, books_details_view, create_books_view, delete_books_view, edit_books_view, create_review_view

urlpatterns = [
    path('name/', name_view, name='name and age'),
    path('hobby/', hobby_view, name='my hobby'),
    path('time/', time_view, name='time'),
    path('', books_view, name='books'),
    path('books/<int:id>/', books_details_view, name='books_details'),
    path('books/<int:id>/delete/', delete_books_view, name='delete_book'),
    path('create_books/', create_books_view, name='create_books'),
    path('books/<int:id>/update/', edit_books_view, name='edit_book'),
    path('books/<int:id>/create_review/', create_review_view, name='create review'),
]