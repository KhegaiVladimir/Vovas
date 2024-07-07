from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListCreateAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieListCreateAPIView.as_view()),]