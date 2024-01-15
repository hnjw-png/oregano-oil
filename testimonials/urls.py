from django.urls import path
from . import views 


urlpatterns = [
    path('testimonial_list/', views.testimonial_list, name='testimonial_list'),
    path('testimonial/<int:testimonial_id>/', views.testimonial_detail, name='testimonial_detail'),
    path('create_testimonial/', views.create_testimonial, name='create_testimonial'),
    path('register_testimonial/<int:testimonial_id>/', views.register_testimonial, name='register_testimonial'),
    path('update_testimonial/<int:testimonial_id>/', views.update_testimonial, name='update_testimonial'),
    path('delete_testimonial/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
]