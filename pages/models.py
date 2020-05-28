from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_id = models.IntegerField()
    unread = models.CharField(max_length=10, default='1')
    title = models.CharField(max_length=100)
    message = models.TextField()
    reference_id = models.IntegerField()
    created_at = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)


class Category(models.Model):
    category = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.category


class blog(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateField()
    banner_big = models.ImageField(upload_to='blog/images', default="")
    banner_smail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title
