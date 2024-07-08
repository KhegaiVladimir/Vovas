from django.contrib import admin
from django.urls import path, include
from movie_app import views
from . import swagger


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', include('movie_app.urls')),
    path('api/v1/directors/', views.DirectorListCreateAPIView.as_view()),
    path('api/v1/user/', include('users.urls')),
    path('api/v1/directors/<int:id>/', views.DirectorRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewListCreateAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/movies/reviews/', views.MovieListCreateAPIView.as_view()),
]


urlpatterns += swagger.urlpatterns