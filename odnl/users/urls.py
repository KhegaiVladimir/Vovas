from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.registration_api_view, name='registration-list'),
    path('authorization/', views.authorization_api_view, name='authorization-list'),
]