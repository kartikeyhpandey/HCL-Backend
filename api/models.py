from django.db import models

class Platform(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #modified_by = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)

class Device(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ipaddress = models.GenericIPAddressField(null=True)
    type = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

class ProductResult(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    connectivity_speed = models.CharField(max_length=50)

class DeviceResult(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE)
    product_result = models.ForeignKey(ProductResult, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    connectivity_speed = models.CharField(max_length=50)