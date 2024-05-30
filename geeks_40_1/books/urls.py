from django.urls import path
from . import views


urlpatterns = [
    path('name/', views.NameView.as_view(), name='name and age'),
    path('hobby/', views.HobbyVIew.as_view(), name='my hobby'),
    path('time/', views.TimeView.as_view(), name='time'),
    path('', views.BooksView.as_view(), name='books'),
    path('books/<int:id>/', views.BooksDetailsView.as_view(), name='books_details'),
    path('books/<int:id>/delete/', views.DeleteBooksView.as_view(), name='delete_book'),
    path('create_books/', views.CreateBookView.as_view(), name='create_books'),
    path('books/<int:id>/update/', views.EditBookView.as_view(), name='edit_book'),
    path('books/<int:id>/create_review/', views.CreateReviewView.as_view(), name='create review'),
]