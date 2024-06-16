from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer


@api_view(['GET'])
def movies_list_api_view(request):
        data = Movie.objects.all()
        list_ = MovieSerializer(data, many=True).data
        return Response(data=list_)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)

@api_view(['GET'])
def directors_list_api_view(request):
    data = Director.objects.all()
    list_ = DirectorSerializer(data, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director does not exist'}, status=status.HTTP_404_NOT_FOUND)
    list_ = DirectorSerializer(director).data
    return Response(data=list_)

@api_view(['GET'])
def reviews_list_api_view(request):
    data = Review.objects.all()
    list_ = ReviewSerializer(data, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        data = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review does not exist'}, status=status.HTTP_404_NOT_FOUND)
    list_ = ReviewSerializer(data).data
    return Response(data=list_)