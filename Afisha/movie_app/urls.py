from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list_api_view),
    path('api/v1/movies/<int:id>/', views.movie_detail_api_view)]