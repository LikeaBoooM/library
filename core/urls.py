
from django.urls import path
from . import views
from . views import CreateBook

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', CreateBook.as_view(), name='create-book' )
    ]