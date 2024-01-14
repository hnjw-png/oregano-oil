from django.urls import path 
from .views import Info, AddLike, AddDislike
from .import views


urlpatterns = [
    path('Info/', views.Info, name='Info'),
    path('AddLike//<int:pk>/', views.AddLike, name='addlike'),
    path('AddDisLike//<int:pk>/', views.AddDislike, name='dislike'),
    
]
