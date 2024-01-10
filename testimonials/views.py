
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Testimonials
from .forms import TestimonialsForm

def Testimonials(request):
    """ A view to return the index page """

    return render(request, 'testimonials/view_testimonials.html')

def CreateTestimonials(request):
    """ A view to return the index page """

    return render(request, 'testimonials/create_testimonial.html')

def TestimonialsListView(request, testimonial_id):
    """ A view to return the index page """
    Testimonials = Testimonials.objects.all()
    return render(request, 'testimonials/list_testimonials.html', {'Testimonials': Testimonials})
   
    
""" a view to create a pre-filled in testimonial form or a blank form, whilst the user is logged in. """

@login_required   
def TestimonialsCreateView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            Testimonials = form.save(commit=False)
            Testimonials.save()
            return redirect('testimonials/view_testimonials', Testimonials_id=Testimonials.id)
    else:
        form = TestimonialsForm()
    return render(request, 'testimonials/testimonials_form.html', {'form': form})

@login_required  
def TestimonialsUpdateView(request, id):
    Testimonials = Testimonials.objects.get(pk=Testimonials_id)
    form = TestimonialsForm(request.POST or None, instance=Testimonials)
    if form.is_valid():
        form.save()
        return redirect('testimonials/testimonial_form', Testimonials_id=Testimonials.id)

    return render(request, 'testimonials/testimonials_form.html', {'testimonial':testimonial, 'form':form})

""" a view to delete a testimonial, whilst logged in. """

@login_required
def TestimonialsDeleteView(request, testimonial_id):
    model = Testimonials
    Testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted!')
    return redirect(reverse('testimonials/testimonial_list'))


