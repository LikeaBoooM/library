from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from . models import Book
from . forms import BookForm

def home(request):
    return render(request, 'core/index.html')


class CreateBook(CreateView):
    model = Book
    template_name = 'core/create-book.html'
    success_url = 'home'
    form_class = BookForm