from django import forms
from .models import Testimonials

class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ['name','title', 'slug', 'description', 'price']
    
    def save(self, commit=True):
        # Get the current user
        user = get_user(self.instance)

        # Set the created_user and updated_user fields
        if not self.instance.pk:  # This is a new testimonial (create)
            self.instance.created_user = user
        self.instance.updated_user = user

        # Call the parent class's save method to save the instance
        instance = super(TestimonialsForm, self).save(commit=commit)

        return instance