from django.db import models

class Books(models.Model):
    GENRES = (
        ('Хоррор', "Хоррор"),
        ("Фантастика", "Фантастика"),
        ("Романтика", "Романтика")
    )

    title = models.CharField(max_length=100, verbose_name='Напишите название книги и т.д.')
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото', blank=True)
    description = models.TextField(verbose_name='НАпишите описание книги')
    music = models.FileField(upload_to='audio/', verbose_name='Загрузите песню', blank=True)
    video = models.URLField(verbose_name='Загрузите ввидео ссылку')
    genre = models.CharField(max_length=100, choices=GENRES, verbose_name='Выберите жанр книги')
    time_books = models.PositiveIntegerField(verbose_name='Укажите время книги')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, verbose_name='Укажите автора книги')
    rate = models.PositiveIntegerField(verbose_name='Укажите среднюю оценку этой книги')

    def __str__(self):
        return f'{self.title} - {self.created_at}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Список книг'