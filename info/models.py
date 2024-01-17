from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LikeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')


    @property
    def total_likes(self):
        return self.likes.count()
    
    @property
    def total_dislikes(self):
        return self.likes.count()
    
   