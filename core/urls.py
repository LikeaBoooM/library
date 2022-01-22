
from django.urls import path
from . import views
from . views import CreateBook, AllBoks, DeleteBook

urlpatterns = [
    path('', AllBoks.as_view(), name='home'),
    path('create/', CreateBook.as_view(), name='create-book'),
    path('delete/<int:pk>/', DeleteBook.as_view(), name='delete-book'),
    ]