from django.urls import path
from . import views

urlpatterns = [
    path("all_cloth/", views.AllClothView.as_view(), name="all_cloth"),
    path("elder_cloth/", views.ElderClothView.as_view(), name="elder_cloth"),
    path("childish_cloth/", views.ChildishClothView.as_view(), name="childish_cloth"),
]
