from django.db import models
from django.contrib import admin

from apps.elements.models import Element
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
    product_operations = models.ManyToManyField(Product, through='Operation')

    def __str__(self):
        return f'{self.name}'


class Operation(models.Model):

    operation = models.ForeignKey(OperationsList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='operations_ref', on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    element_quantity = models.IntegerField(max_length=30)
    time_processing = models.IntegerField(max_length=100)

    def __str__(self):
        return f'{self.operation.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save()
        product = Product.objects.get(id=self.product.id)
        product.save()

    def delete(self, using=None, keep_parents=False):
        product = Product.objects.get(id=self.product.id)
        product.product_time_production = str(int(product.product_time_production) - self.time_processing)
        super().delete()
        product.save()


class OperationsInline(admin.TabularInline):
    model = Operation
