from django.urls import path
from . import views
from .views import product_view, images_by_product_name

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('product/', product_view, name='product'),
    path('images/', images_by_product_name, name='images_by_product_name'),


]

