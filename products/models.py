from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField()

    class Meta: ordering = ('name',)

    def _str_(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-created_at',)

    def _str_(self):
        return self.name

        

