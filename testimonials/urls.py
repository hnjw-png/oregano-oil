from django.urls import path
from . import views

urlpatterns = [
    path('ListView/', views.TestimonialsListView, name='TestimonialsListView'),
    path('CreateView/', views.TestimonialsCreateView, name='TestimonialsCreateView'),
    path('UpdateView/', views.TestimonialsUpdateView, name='TestimonialsUpdateView'),
    path('DeleteView/', views.TestimonialsDeleteView, name='TestimonialsDeleteView'),
    path('', views.view_testimonials, name='testimonials')
]

