from django.db import models
from django.utils import timezone


class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Post(models.Model):

    title = models.CharField(max_length=250)
    pub_date = models.DateField(default=timezone.now())
    content = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
