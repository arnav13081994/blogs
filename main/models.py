from django.db import models
from django.urls import reverse


# Create your models here.


class Author(models.Model):
    DESIGNATION = (
        ('Admin', 'Admin'),
        ('Author', 'Author'),
    )
    name = models.CharField(max_length=256)
    designation = models.CharField(choices=DESIGNATION, max_length= 100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    thumbnail = models.ImageField(default='static/main/images/article_generic.jpeg')

    authors = models.ManyToManyField("Author")

    @property
    def get_text_preview(self):
        return ' '.join(self.content.split()[:20])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:article', kwargs={'pk': self.id})

