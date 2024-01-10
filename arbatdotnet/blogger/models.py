from django.db import models
from django.utils import timezone

class Blogger(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    fullname = models.CharField(default='', max_length=25)
    description = models.TextField()
    def __str__(self):
        return self.username
class Article(models.Model):
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    title = models.CharField(default='',max_length=250)
    body = models.TextField(default='')
    views = models.TextField(default='0')
    likes = models.TextField(default='0')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title