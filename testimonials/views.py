from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

class TestimonialsListView(ListView):
    model = Testimonials
    template_name = 'testimonials/list_testimonials.html'  # Create this template to display the list of events
    context_object_name = 'events'

@login_required
class TestimonialsCreateView(CreateView):
    model = Testimonials
    form_class = TestimonialsForm
    template_name = 'Testimonials/forms.py'  # Create this template for the event creation form
    success_url = reverse_lazy('event_list')  # Redirect to the event list after successful creation

@login_required
class EventUpdateView(UpdateView):
    model = Testimonials
    form_class = TestimonialsForm
    template_name = 'testimonial/testimonial_form.html'  # Create this template for the event update form
    context_object_name = 'Testimonial'  # Set the context object name
    success_url = reverse_lazy('list_testimonials')  # Redirect to the event list after successful update

@login_required
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'testimonial/testimonial_confirm_delete.html'  # Create this template for the delete confirmation page
    context_object_name = 'testimonial'  # Set the context object name
    success_url = reverse_lazy('list_testimonial')  # Redirect to the event list after successful deletion