from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product-list'),
    path('api/v1/products/<int:id>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product'),
    path('api/v1/reviews/', views.ReviewListCreateView.as_view(), name='reviews'),
    path('api/v1/reviews/<int:id>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review')
]