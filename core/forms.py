
from . models import Book
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'autor', 'date_publish', 'ISBN_number', 'counts_page', 'link_poster', 'language',]
        widgets = {
            'date_publish': DateInput(),
        }


