from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Testimonials
from .forms import TestimonialsForm

@login_required
def add_testimonial(request):
    """ Add a Testimonial to the store """
    if request.method == 'POST':
        form = TestimonialsForm(request.POST, request.FILES)
        if form.is_valid():
            Testimonials = form.save()
            messages.success(request, 'Successfully added Testimonial!')
            return redirect(reverse('testimonial', args=[Testimonials.id]))
        else:
            messages.error(request, 'Failed to add Testimonial. Please ensure the form is valid.')
    else:
        form = TestimonialsForm()
        
    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)