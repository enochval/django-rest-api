from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product-list'),
    path('products/info/', views.product_info, name='product-info'),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view(), name='get-product'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list')
]