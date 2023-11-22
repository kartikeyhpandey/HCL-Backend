from django.urls import path
from .views import (
    PlatformListCreateView, PlatformDetailView,
    ProductListCreateView, ProductDetailView,
    DeviceListCreateView, DeviceDetailView, ProductResultListView,
    ProductResultDetailView, DeviceResultListView, DeviceResultDetailView
)

urlpatterns = [
    path('platforms/', PlatformListCreateView.as_view(), name='platform-list-create'),
    path('platforms/<pk>/', PlatformDetailView.as_view(), name='platform-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('product-results/', ProductResultListView.as_view(), name='product-result-list'),
    path('product-results/<int:pk>/', ProductResultDetailView.as_view(), name='product-result-detail'),
    path('device-results/', DeviceResultListView.as_view(), name='device-result-list'),
    path('device-results/<int:pk>/', DeviceResultDetailView.as_view(), name='device-result-detail'),

]
