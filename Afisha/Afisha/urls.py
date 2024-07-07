from django.contrib import admin
from django.urls import path, include
from movie_app import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/movies/', views.movies_list_api_view),
#     path('api/v1/movies/<int:id>/', views.movie_detail_api_view),
#     path('api/v1/directors/', views.directors_list_api_view),
#     path('api/v1/directors/<int:id>/', views.director_detail_api_view),
#     path('api/v1/reviews/', views.reviews_list_api_view),
#     path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
#     path('api/v1/movies/reviews/', views.movies_reviews_list_api_view),
# ]
#

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
