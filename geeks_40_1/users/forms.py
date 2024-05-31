from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'favourite_book',
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

@receiver(post_save, sender=models.CustomUser)
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