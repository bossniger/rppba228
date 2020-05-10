from django.db import models


class Order(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(max_length=10)