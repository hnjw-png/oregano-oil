from django.contrib import admin
from .models import Testimonials
admin.site.register

@admin.register(Testimonials)
class Testimonials(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')