from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-created_at',)
        

    def _str_(self):
        return self.name

        
class Image(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
