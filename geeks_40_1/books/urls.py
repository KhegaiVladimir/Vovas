from django.urls import path
from .views import name_view, hobby_view, time_view

urlpatterns = [
    path('name/', name_view, name='name and age'),
    path('hobby/', hobby_view, name='my hobby'),
    path('time', time_view, name='time')
]
