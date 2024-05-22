from django.urls import path
from . import views

urlpatterns = [
    path('all_cloth/', views.all_cloth, name='all_cloth'),
    path('male_cloth/', views.male_cloth, name='male_cloth'),
    path('female_cloth/', views.female_cloth, name='female_cloth'),
    path('child_cloth/', views.child_cloth, name='child_cloth'),
]