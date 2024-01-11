from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LikeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, blank=True)

def number_of_likes(self):
        return self.likes.count()

