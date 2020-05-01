from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=None, max_digits=15, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'



class Publisher(models.Model):
    title = models.CharField(max_length=50)
    year_of_foundation = models.SmallIntegerField()
    city_of_location = models.CharField(max_length=50)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'