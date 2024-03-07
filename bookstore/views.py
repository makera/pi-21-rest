from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
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
    permission_classes = [DjangoModelPermissions]

    @action(methods=['GET'], detail=False)
    def bestsellers(self, request):
        print(request.user)
        qs = self.get_queryset().filter(year_create__gte=1820)
        serializer = self.get_serializer_class()(qs, many=True)
        return Response(data=serializer.data)

    @action(methods=['POST'], detail=True)
    def take(self, request, pk):
        return Response(data={'status': 'ok'}, status=200)
