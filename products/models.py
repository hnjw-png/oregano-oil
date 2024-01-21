from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='', default='media/images/default.jpg')

    class Meta:
        ordering = ('-created_at',)
        

    def _str_(self):
        return self.name



class rate(models.Model):
    #User = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
   
    def __str__(self):
        return str(self)
              
