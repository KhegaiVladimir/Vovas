# Generated by Django 5.0.6 on 2024-06-01 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="review_book",
            new_name="review_item",
        ),
    ]
