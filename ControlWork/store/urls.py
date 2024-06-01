from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
    path("info/", views.InformationView.as_view(), name="info"),
    path("items/<int:id>/", views.ItemDetailsView.as_view(), name="item-details"),
    path("items/", views.AllItemsView.as_view(), name="items"),
    path("items/create_review/", views.CreateReviewView.as_view(), name="create review"),
]
