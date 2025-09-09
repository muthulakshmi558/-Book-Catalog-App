from django.shortcuts import render
from .models import Book

# -------------------- Django Template View --------------------
def book_list(request):
    """
    Render the list of books in an HTML template.
    """
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


# -------------------- Django REST Framework API --------------------
from rest_framework import generics, filters
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint to list all books (GET),
    add a new book (POST), and search by title/genre.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre']
