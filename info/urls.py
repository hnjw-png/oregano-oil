from django.urls import path 
from .views import Info, AddLike, AddDislike
from .import views


urlpatterns = [
    path('Info/', views.Info, name='Info'),
    path('info/<int:pk>/AddLike', views.AddLike, name='addlike'),
    path('info/<int:pk>/AddDisLike', views.AddDislike, name='dislike'),
    
]
