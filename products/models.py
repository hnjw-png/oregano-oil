from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField()

    class Meta: ordering = ('name',)

    def _str_(self):
        return self.name
