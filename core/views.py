from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . models import Book
from . forms import BookForm
from django.db.models import Q
from rest_framework.views import APIView
from . serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from . getData import getdata

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
    template_name = 'core/book-update.html'
    success_url = '/'
    fields = '__all__'


class SearchBook(ListView):
    model = Book
    template_name = 'core/search-book.html'

    def get_queryset(self):
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')
        language = self.request.GET.get('language')
        datest = self.request.GET.get('datest')
        datend = self.request.GET.get('datend')
        if datest == "" or datend == "":
            datest = '1000-01-01'
            datend = '3000-01-01'
            object_list = Book.objects.filter(
                Q(title__icontains=title) & Q(autor__icontains=author) &
                Q(language__icontains=language) & Q(date_publish__range=(datest, datend)))
            return object_list
        else:
            object_list = Book.objects.filter(
                Q(title__icontains=title) & Q(autor__icontains=author) &
                Q(language__icontains=language) & Q(date_publish__range=(datest, datend)))
            return object_list


class SearchBooksAPI(APIView):
    def get(self, request):
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')
        language = self.request.GET.get('language')
        datest = self.request.GET.get('datest')
        datend = self.request.GET.get('datend')
        if datest == "" or datend == "":
            datest = '1000-01-01'
            datend = '3000-01-01'
            object_list = Book.objects.filter(
                Q(title__icontains=title) & Q(autor__icontains=author) &
                Q(language__icontains=language) & Q(date_publish__range=(datest, datend)))
            serializer = BookSerializer(object_list, many=True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            object_list = Book.objects.filter(
                Q(title__icontains=title) & Q(autor__icontains=author) &
                Q(language__icontains=language) & Q(date_publish__range=(datest, datend)))
            serializer = BookSerializer(object_list, many=True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class SearchGoogleAPI(APIView):
    model = Book
    template_name = 'core/search-book.html'

    def get(self, request):
        arguments = []
        q = self.request.GET.get('q')
        intitle = self.request.GET.get('intitle')
        inautor = self.request.GET.get('inauthor')
        inpublisher = self.request.GET.get('inpublisher')
        subject = self.request.GET.get('subject')
        isbn = self.request.GET.get('isbn')
        lccn = self.request.GET.get('lccn')
        oclc = self.request.GET.get('oclc')

        arguments.extend((q, intitle, inautor, inpublisher, subject, isbn, lccn, oclc))
        getdata(arguments)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

