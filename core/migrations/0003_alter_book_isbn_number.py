# Generated by Django 3.2.11 on 2022-01-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN_number',
            field=models.IntegerField(unique=True),
        ),
    ]
