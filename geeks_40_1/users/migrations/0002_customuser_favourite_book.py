# Generated by Django 5.0.6 on 2024-05-31 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="favourite_book",
            field=models.CharField(default="Нет", max_length=100),
        ),
    ]
