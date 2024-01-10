from django.urls import path
from . import views


urlpatterns = [
    path('ListView/', views.TestimonialsListView, name='TestimonialsListView'),
    path('TestimonialsCreateView/', views.TestimonialsCreateView, name='TestimonialsCreateView'),
    path('TestimonialsUpdateView//<int:testimonial_id>/', views.TestimonialsUpdateView, name='TestimonialsUpdateView'),
    path('TestimonialsDeleteView//<int:testimonial_id>/', views.TestimonialsDeleteView, name='TestimonialsDeleteView'),
    path('Testimonials', views.Testimonials, name='Testimonials'),
    path('CreateTestimonials', views.CreateTestimonials, name ='CreateTestimonials'),
]
