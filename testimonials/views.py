from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Testimonials
from .forms import TestimonialsForm



def Testimonial(request):
    """ A view to return the index page """

    return render(request, 'testimonials/view_testimonials')

class TestimonialsListView(ListView):
    model = Testimonials
    template_name = 'testimonials/list_testimonials.html'  # Create this template to display the list of events
    context_object_name = 'Testimonials info'

@login_required
class TestimonialsCreateView(CreateView):
    model = Testimonials
    form_class = TestimonialsForm
    template_name = 'testimonials/create_testimonials.html'  # Create this template for the testimonial creation form
    success_url = reverse_lazy('testimonial_list')  # Redirect to the testimonial list after successful creation

@login_required
class TestimonialsUpdateView(UpdateView):
    model = Testimonials
    form_class = TestimonialsForm
    template_name = 'testimonial/edit_testimonials.html'  # Create this template for the testimonial update form
    context_object_name = 'Testimonial'  # Set the testimonial name
    success_url = reverse_lazy('list_testimonials')  # Redirect to the testimonial list after successful update

@login_required
class TestimonialsDeleteView(DeleteView):
    model = Event
    template_name = 'testimonial/testimonial_confirm_delete.html'  # Create this template for the delete a testimonial page
    context_object_name = 'testimonial'  # Set the context object name
    success_url = reverse_lazy('list_testimonial')  # Redirect to the testimonial list after successful deletion