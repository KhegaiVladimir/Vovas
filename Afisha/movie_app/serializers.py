from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Movie, Director, Review



class DirectorsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title')

    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie_title']


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.stars for review in reviews if review.stars is not None) / len(reviews)
        return None

class DirectorsSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def get_movies_count(self, obj):
        return obj.movies.count()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(min_length=1, max_length=200)
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, category_id):
        try:
            Director.objects.get(id=category_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exist')
        return category_id

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=100)

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=200)
    stars = serializers.IntegerField()
    movie_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exist')
        return movie_id
