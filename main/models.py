from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#
# @receiver(post_save, sender=Author)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
#

class Article(models.Model):
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    thumbnail = models.ImageField(default='static/main/images/article_generic.jpeg')

    authors = models.ManyToManyField("Author")

    @property
    def get_text_preview(self):
        return self.content[:100] # in order to better align the cards count by characters instead

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:article', kwargs={'pk': self.id})

