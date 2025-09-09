from django.urls import path
from . import views
from .views import BookListAPIView, book_list


urlpatterns = [
    path('', book_list, name='book_list'),
    path('api/books/', BookListAPIView.as_view(), name='book_list_api'),

]
