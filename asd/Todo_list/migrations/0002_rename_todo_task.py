# Generated by Django 5.0.7 on 2024-08-03 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Task',
        ),
    ]
