from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Devis(models.Model):
    title = models.CharField(max_length=50)


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(verbose_name="Напишите описание")
    price = models.PositiveIntegerField(default=100)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return f"{self.name}"


class VideoContent(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.title


class Review(models.Model):
    review_item = models.ForeignKey(
        Items, on_delete=models.CASCADE, related_name="review_book"
    )
    stars = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.review_item} - {self.stars} stars"