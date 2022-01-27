from django.db import models
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    date_publish = models.DateField(blank=True, null=True)
    ISBN_number = models.CharField(max_length=100)
    counts_page = models.IntegerField()
    link_poster = models.CharField(max_length=1000)
    language = models.CharField(max_length=100)

    def __str__(self):
        return f'({self.autor} + {self.title})'


class Search(models.Model):
    q = models.CharField(max_length=100)
    intitle = models.CharField(max_length=100)
    inautor = models.CharField(max_length=100)
    inpublisher = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    lccn = models.CharField(max_length=100)
    oclc = models.CharField(max_length=100)

    def __str__(self):
        return f'({self.q})'
