from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class LikeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    dislikes = models.ManyToManyField(User, related_name='dislikes')
    
    
    @property
    def total_likes_received(self):
        total_likes_received = likes.objects.filter.count()
        return self.total_likes_received.count()
    
    
    
    @property
    def total_dislikes_received(self):
        total_dislikes_received = dislikes.objects.filter.count()
        return self.total_dislikes_received.count()
    
    
   