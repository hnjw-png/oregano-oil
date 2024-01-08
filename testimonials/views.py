
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

def TestimonialsListView(ListView):
    """ A view to return the index page """

    return render(request, 'testimonials/list_testimonials.html')
    
""" a view to create a pre-filled in testimonial form or a blank form, whilst the user is logged in. """

@login_required   
def TestimonialsCreateView(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        """ create a form instance, and fill it wite testimonial information from that request """
        
        form = TestimonialsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return messages.success(request, 'Testimonial created!')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestimonialsForm()

    return render(request, "create_testimonials.html", {"form": form})

""" a view to update or edit a existing testimonial, whilst the user  is logged in. """

@login_required  
def TestimonialsUpdateView(request, id):
    model = Testimonials
    Testimonial = get_object_or_404(Testimonials, id=testimonial_id)

    if request.method == 'GET':
        context = {'form': TestimonialsForm(instance=post), 'id': id}
        return render(request,'testimonials/edit_testimonials.html',context)

""" a view to delete a testimonial, whilst logged in. """

@login_required
def TestimonialsDeleteView(request, testimonial_id):
    model = Testimonials
    Testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted!')
    return redirect(reverse('testimonial_list'))