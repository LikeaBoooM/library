from django.db import models
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    autor = models.CharField(max_length=100)
    date_publish = models.DateField(blank=True, null=True)
    ISBN_number = models.IntegerField(unique=True)
    counts_page = models.IntegerField()
    link_poster = models.CharField(max_length=1000)
    language = models.CharField(max_length=100)

    def __str__(self):
        return f'({self.autor} + {self.title})'
