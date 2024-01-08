from django.urls import path
from . import views

urlpatterns = [
    path('ListView/', views.TestimonialsListView, name='TestimonialsListView'),
    path('CreateView/', views.TestimonialsCreateView, name='TestimonialsCreateView'),
    path('UpdateView//<int:testimonial_id>/', views.TestimonialsUpdateView, name='TestimonialsUpdateView'),
    path('DeleteView//<int:testimonial_id>/', views.TestimonialsDeleteView, name='TestimonialsDeleteView'),
    path('Testimonials/', views.view_Testimonials, name='Testimonials'),
]
