
from django.urls import path
from . import views
from . views import CreateBook, AllBoks, DeleteBook, UpdateBook, SearchBook, SearchBooksAPI, SearchGoogleAPI

urlpatterns = [
    path('', AllBoks.as_view(), name='home'),
    path('create/', CreateBook.as_view(), name='create-book'),
    path('delete/<int:pk>/', DeleteBook.as_view(), name='delete-book'),
    path('update/<int:pk>/', UpdateBook.as_view(), name='update-book'),
    path('search/', SearchBook.as_view(), name='search-book'),
    path('searchAPI/', SearchBooksAPI.as_view(), name='search-book-api'),
    path('searchAPIGoogle/', SearchGoogleAPI.as_view(), name='search-book-google-api'),

]