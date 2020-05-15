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
