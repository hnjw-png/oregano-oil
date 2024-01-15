from django.urls import path 
from .views import Info, AddLike, AddDislike
from .import views


urlpatterns = [
    path('Info/', views.Info, name='Info'),
    path('AddLike/', views.AddLike, name='addlike'),
    path('AddDisLike/', views.AddDislike, name='dislike'),
    
]
