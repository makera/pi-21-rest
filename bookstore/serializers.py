from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'birthday', 'died')


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name')

    class Meta:
        model = Book
        fields = ('id', 'author', 'name', 'published_by', 'year_create', 'sheets', 'author_name',)
