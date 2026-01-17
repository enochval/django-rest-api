from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.get_product, name='get-product'),
    path('orders/', views.order_list, name='order-list')
]