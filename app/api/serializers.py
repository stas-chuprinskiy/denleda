from api.models import Author, Book
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "birth_date",
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "author",
            "description",
            "pub_date",
        )

    def create(self, validated_data):
        book = super().create(validated_data)
        user = self.context.get("request").user
        author, _ = Author.objects.get_or_create(
            first_name=user.first_name,
            last_name=user.last_name,
            birth_date=user.birth_date,
        )
        book.author = author
        book.save()
        return book
