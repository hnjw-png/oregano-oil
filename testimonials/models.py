from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Testimonials(models.Model):
    title = models.CharField(max_length=255, default="testimonial")
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    
    def _str_(self):
        return self.title

        
