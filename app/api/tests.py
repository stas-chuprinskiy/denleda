from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book
from api.serializers import BookSerializer

User = get_user_model()


class CreateBookTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="adm_username",
            password="adm_password",
        )
        self.client.force_authenticate(self.user)
        self.data = {
            "name": "Тестовая книга",
            "description": "Описание тестовой книги",
        }

    def test_create_book(self):
        response = self.client.post(reverse("books-list"), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().name, "Тестовая книга")


class GetBookTestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Автор",
            last_name="Авторович",
        )
        self.book = Book.objects.create(
            name="Тестовая книга",
            author=self.author,
            description="Описание тестовой книги",
        )

    def test_get_book_list(self):
        response = self.client.get(reverse("books-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get("name"), "Тестовая книга")

    def test_get_book_detail(self):
        response = self.client.get(
            reverse("books-detail", args=[self.book.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "Тестовая книга")


class PutBookTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="adm_username",
            password="adm_password",
        )
        self.client.force_authenticate(self.user)
        self.author = Author.objects.create(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
        )
        self.book = Book.objects.create(
            name="Тестовая книга",
            author=self.author,
            description="Описание тестовой книги",
        )
        self.data = BookSerializer(self.book).data
        self.data.update(
            {
                "name": "Измененная книга",
                "description": "Измененное описание книги",
            }
        )

    def test_put_book(self):
        response = self.client.put(
            reverse("books-detail", args=[self.book.id]),
            self.data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "Измененная книга")
        self.assertEqual(
            response.data.get("description"), "Измененное описание книги"
        )


class DeleteBookTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="adm_username",
            password="adm_password",
        )
        self.client.force_authenticate(self.user)
        self.author = Author.objects.create(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
        )
        self.book = Book.objects.create(
            name="Тестовая книга",
            author=self.author,
            description="Описание тестовой книги",
        )

    def test_delete_book(self):
        response = self.client.delete(
            reverse("books-detail", args=[self.book.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
