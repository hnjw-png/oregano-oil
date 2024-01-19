from django.urls import path 
from .views import Info, AddLike, AddDislike
from .import views


urlpatterns = [
    path('Info/', views.Info, name='Info'),
    path('AddLike/', views.AddLike, name='likes'),
    path('AddDislike/', views.AddDislike, name='dislikes'),

]
