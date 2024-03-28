from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, BookViewSet, BookList

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', BookList.as_view())
]
