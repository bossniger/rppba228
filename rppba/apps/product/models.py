from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    time_processing = models.DecimalField(max_digits=10, decimal_places=0)


class Material(models.Model):
    material_name = models.CharField(max_length=50)


class Component(models.Model):
    component_name = models.CharField(max_length=50)
