from rest_framework.viewsets import ModelViewSet
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ('get',)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ('get', 'post', 'put')
