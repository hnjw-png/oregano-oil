from django import forms
from .models import Testimonials

class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ['name','title', 'slug', 'description', 'price']
    
    