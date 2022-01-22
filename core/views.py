from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . models import Book
from . forms import BookForm

def home(request):
    return render(request, 'core/index.html')


class CreateBook(CreateView):
    model = Book
    template_name = 'core/create-book.html'
    success_url = '/'
    form_class = BookForm


class AllBoks(ListView):
    model = Book
    template_name = 'core/all-books.html'


class DeleteBook(DeleteView):
    model = Book
    success_url = '/'
    template_name = 'core/book-delete.html'


class UpdateBook(UpdateView):
    model = Book
    tem
    success_url = '/all-books'