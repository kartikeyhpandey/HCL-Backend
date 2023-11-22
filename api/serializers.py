from rest_framework import serializers
from .models import Platform, Product, Device, ProductResult, DeviceResult

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    platform = serializers.PrimaryKeyRelatedField(queryset=Platform.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Device
        fields = '__all__'

class DeviceResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceResult
        fields = '__all__'

class ProductResultSerializer(serializers.ModelSerializer):
    devices = DeviceResultSerializer(many=True, read_only=True)

    class Meta:
        model = ProductResult
        fields = ['product', 'status', 'connectivity_speed', 'devices']