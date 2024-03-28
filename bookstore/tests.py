from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User
from .serializers import BookSerializer


class BooksTests(APITestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(name='author')
        self.book1 = Book.objects.create(name='book', year_create=2000, author=self.author, published_by='pub',
                                         sheets=50, )
        self.user = User.objects.create_user('test', 'test@test.ru')

    def test_anonymous_user(self):
        response = self.client.get('/api/books/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_books_list(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/books/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        serializer = BookSerializer(Book.objects.all(), many=True)
        self.assertListEqual(response.data, serializer.data)

    def test_get_book(self):
        self.client.force_login(self.user)
        response = self.client.get(f'/api/books/{self.book1.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BookSerializer(Book.objects.get(id=self.book1.id))
        self.assertDictEqual(response.data, serializer.data)


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['books.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_book_page(self):
        self.selenium.get(f"{self.live_server_url}/")
        elements = self.selenium.find_elements(By.XPATH, '//div')
        for element in elements:
            self.assertIn(element.text, list(map(lambda b: b.name, Book.objects.all())))
