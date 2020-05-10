from django.db import models
from django.contrib import admin

from apps.products.models import Product


class OperationsList(models.Model):

    TYPE_CHOICE = (
        ('1', '1'),
        ('2', '2',),
        ('3', '3',),
        ('4', '4',),
    )

    name = models.CharField(max_length=30)
    priority = models.CharField(max_length=50, choices=TYPE_CHOICE)
    product_operations = models.ManyToManyField(Product, through='Operations')

    def __str__(self):
        return f'{self.name}'


class Operations(models.Model):

    operation = models.ForeignKey(OperationsList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time_processing = models.IntegerField(max_length=100)

    def __str__(self):
        return f'{self.operation.name}'


class OperationsInline(admin.TabularInline):
    model = Operations
