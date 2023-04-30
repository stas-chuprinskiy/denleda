from django.db import models


class Author(models.Model):
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    birth_date = models.DateField("Дата рождения", blank=True, null=True)

    class Meta:
        ordering = ("-id",)
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.CharField("Название", max_length=150)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        related_name="books",
        verbose_name="Автор",
        blank=True,
        null=True,
    )
    description = models.TextField("Описание", blank=True, null=True)
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True, editable=False
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"({self.id}) {self.name}"
