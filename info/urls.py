from django.urls import path
from .import views 

urlpatterns = [
    path('Info', views.Info, name='Info'),
    path('like/<slug:slug>', views.like, name='like'),
]

