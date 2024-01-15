from django.contrib import admin

# Register your models here.

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'price',
        
    )
