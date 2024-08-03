from rest_framework import serializers
from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'rating', 'product']

class ProductSerializer(serializers.ModelSerializer):
    product_reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'product_reviews']