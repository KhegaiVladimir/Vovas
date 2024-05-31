from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Books(models.Model):
    GENRES = (
        ("Хоррор", "Хоррор"),
        ("Фантастика", "Фантастика"),
        ("Романтика", "Романтика"),
    )
    title = models.CharField(
        max_length=100, verbose_name="Напишите название книги и т.д.", null=True
    )
    image = models.ImageField(
        upload_to="images/", verbose_name="Загрузите фото", blank=True, null=True
    )
    description = models.TextField(verbose_name="НАпишите описание книги")
    music = models.FileField(
        upload_to="audio/", verbose_name="Загрузите песню", blank=True, null=True
    )
    video = models.URLField(verbose_name="Загрузите ввидео ссылку")
    genre = models.CharField(
        max_length=100, choices=GENRES, verbose_name="Выберите жанр книги", null=True
    )
    time_books = models.PositiveIntegerField(
        verbose_name="Укажите время книги", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    author = models.CharField(
        max_length=100, verbose_name="Укажите автора книги", null=True
    )
    rate = models.PositiveIntegerField(
        verbose_name="Укажите среднюю оценку этой книги", null=True
    )

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Список книг"
        verbose_name_plural = "Список книг"


class Review(models.Model):
    review_book = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name="review_book"
    )
    stars = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.review_book} - {self.stars} stars"
