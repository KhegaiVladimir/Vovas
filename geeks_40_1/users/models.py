from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveSmallIntegerField(default=19, validators = [MinValueValidator(5), MaxValueValidator(90)])
    gender = models.CharField(max_length=50, choices=GENDER)
    allowed_ganres = models.CharField(max_length=50, default='Не определенно')
    favourite_book = models.CharField(max_length=100, default='Нет')

@receiver(post_save, sender=CustomUser)
def set_allowed_ganres(sender, instance, created, **kwargs):
    if created:
        print("Пользователь создан")
        age = instance.age
        if age < 5:
            instance.allowed_ganres = "Сказки"
        elif age >=5  and age<= 10:
            instance.allowed_ganres = "Сказки"
        elif age >=10 and age<= 18:
            instance.allowed_ganres = "Фантастика"
        elif age >=19 and age<= 45:
            instance.allowed_ganres = "Художественная Литература"
        else:
            instance.allowed_ganres = "Клуб не определен"
        instance.save()