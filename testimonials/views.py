
from django. shortcuts import render, get_object_or_404, redirect
from django. views import generic
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .models import Testimonials
from .forms import TestimonialsForm


def testimonial_list(request):
    testimonials = Testimonials.objects.all()
    return render(request, 'testimonials/testimonials_list.html', {'testimonials': testimonials})

def testimonial_detail(request, testimonial_id):
    testimonial = get_object_or_404(Testimonials, pk=testimonial_id)
    return render(request, 'testimonials/testimonial_detail.html', {'testimonial': testimonial})

@login_required
def create_testimonial(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.organizer = request.user
            testimonial.save()
            return redirect('testimonial_detail', testimonial_id=testimonial.id)
    else:
        form = TestimonialsForm()
    return render(request, 'testimonials/testimonial_form.html', {'form': form})

#@login_required
#def register_testimonial(request, testimonial_id):
#    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
#    return redirect('testimonial_detail', testimonial_id=testimonial.id)
    

@login_required
def delete_testimonial(request, testimonial_id):
    testimonial = Testimonials.objects.get(pk=testimonial_id)
    testimonial.delete()
    return redirect('testimonial_list')


@login_required
def update_testimonial(request, testimonial_id):
    testimonial = Testimonials.objects.get(pk=testimonial_id)
    form = TestimonialsForm(request.POST or None, instance=testimonial)
    if form.is_valid():
        form.save()
        return redirect('testimonial_form', testimonial_id=testimonial.id)

    return render(request, 'testimonials/testimonial_form.html', {'testimonial':testimonial, 'form':form})