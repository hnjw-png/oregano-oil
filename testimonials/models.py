from django.db import models

# Create your models here.

class Testimonials(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    
    def _str_(self):
        return self.name

        
