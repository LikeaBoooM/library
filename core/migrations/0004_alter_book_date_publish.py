# Generated by Django 3.2.11 on 2022-01-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_book_isbn_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_publish',
            field=models.DateField(blank=True, null=True),
        ),
    ]