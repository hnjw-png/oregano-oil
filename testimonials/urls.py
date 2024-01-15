from django.urls import path
from . import views 


urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('reservation/<int:testimonial_id>/', views.reservation_detail, name='reservation_detail'),
    path('create_testimonial/', views.create_testimonial, name='create_testimonial'),
    path('register_testimonial/<int:testimonial_id>/', views.register_testimonial, name='register_testimonial'),
    path('update_testimonial/<int:testimonial_id>/', views.update_testimonial, name='update_testimonial'),
    path('delete_testimonial/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]