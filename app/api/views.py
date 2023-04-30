from api.models import Book
from api.serializers import BookSerializer
from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get", "post", "put", "delete"]
