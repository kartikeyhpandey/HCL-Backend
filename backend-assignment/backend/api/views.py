from rest_framework import generics
from .models import Platform, Product, Device, ProductResult, DeviceResult
from .serializers import PlatformSerializer, ProductSerializer, DeviceSerializer, ProductResultSerializer, DeviceResultSerializer

class PlatformListCreateView(generics.ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer 

    def perform_create(self, serializer):
        serializer.save()   

class PlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Automatically associate the product with the correct platform
        platform_id = self.request.data.get('platform')
        platform_instance = Platform.objects.get(pk=platform_id)
        serializer.save(platform=platform_instance)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def perform_create(self, serializer):
        # Automatically associate the device with the correct product
        product_id = self.request.data.get('product')
        product_instance = Product.objects.get(pk=product_id)
        serializer.save(product=product_instance)

class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class ProductResultListView(generics.ListCreateAPIView):
    queryset = ProductResult.objects.all()
    serializer_class = ProductResultSerializer

class ProductResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductResult.objects.all()
    serializer_class = ProductResultSerializer

class DeviceResultListView(generics.ListCreateAPIView):
    queryset = DeviceResult.objects.all()
    serializer_class = DeviceResultSerializer

class DeviceResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceResult.objects.all()
    serializer_class = DeviceResultSerializer