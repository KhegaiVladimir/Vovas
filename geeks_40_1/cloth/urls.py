from django.urls import path
from . import views

urlpatterns = [
    path('all_cloth/', views.AllClothView.as_view(), name='all_cloth'),
    path('male_cloth/', views.MaleClothView.as_view(), name='male_cloth'),
    path('female_cloth/', views.FemaleClothView.as_view(), name='female_cloth'),
    path('child_cloth/', views.ChildClothView.as_view(), name='child_cloth'),
]