import datetime

from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    birthday = models.DateField(verbose_name='Дата рождения', default=datetime.date.today)
    died = models.DateField(verbose_name='Дата смерти', blank=True, null=True)

    def __str__(self):
        return self.name


def current_year():
    return datetime.date.today().year


class Book(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    year_create = models.IntegerField(verbose_name='Год написания')
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE)
    published_by = models.CharField(verbose_name='Издатель', max_length=50)
    year_published = models.IntegerField(verbose_name='Год издания', default=current_year)
    sheets = models.IntegerField(verbose_name='Кол-во страниц')
