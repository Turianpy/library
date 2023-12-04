from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from books.models import Book

from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
