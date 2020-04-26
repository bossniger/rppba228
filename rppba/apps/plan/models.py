from django.db import models
from ..product.models import Product


class Plan(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10)
