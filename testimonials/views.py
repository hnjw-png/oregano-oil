
from django. shortcuts import render, get_object_or_404, redirect
from django. views import generic
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .models import Reservation, Client
from .forms import ReservationForm

#def Reservation(request):
 #   return render(request, 'bookingblog/index.html')

def testimonial_list(request):
    testimonials = Testimonials.objects.all()
    return render(request, 'testimonial_list.html', {'testimonials': testimonials})

def testimonial_detail(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, pk=reservation_id)
    return render(request, 'testimonial_detail.html', {'testimonial': testimonial})

@login_required
def create_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.save()
            return redirect('testimonial_detail', testimonial_id=testimonial.id)
    else:
        form = TestimonialsForm()
    return render(request, 'testimonial_form.html', {'form': form})

@login_required
def register_testimonial(request, reservation_id):
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    return redirect('testimonial_detail', testimonial_id=testimonial.id)
    

@login_required
def delete_testimonial(request, testimonial_id):
    testimonial = Testimonial.objects.get(pk=testimonial_id)
    testimonial.delete()
    return redirect('testimonial_list')
