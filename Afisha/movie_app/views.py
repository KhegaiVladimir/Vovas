from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorsInfoSerializer, ReviewSerializer, DirectorsSerializer,MovieValidateSerializer, DirectorValidateSerializer


@api_view(['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
        data = Movie.objects.all()
        list_ = MovieSerializer(data, many=True).data
        return Response(data=list_)

    elif request.method == 'POST':  #добавление объекта
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )

        return Response(data={'movie_id': movie.id, 'title': movie.title}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'PUT':  #изменение объекта
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.save()

        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        list_ = DirectorsSerializer(directors, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        list_ = DirectorsInfoSerializer(director).data
        return Response(data=list_)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director.name = serializer.validated_data   .get('name')
        director.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        data = Review.objects.all()
        list_ = ReviewSerializer(data, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        list_ = ReviewSerializer(review).data
        return Response(data=list_)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movies_reviews_list_api_view(request):
    data = Movie.objects.prefetch_related('reviews').all()
    list_ = MovieSerializer(data, many=True).data
    return Response(data=list_)



