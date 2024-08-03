from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_reviews', blank=True, null=True)

    def __str__(self):
        return self.text

class Product(models.Model):
    title = models.CharField(max_length=100)
    price =models.FloatField()
    description = models.TextField()




    def __str__(self):
        return self.title




