from django.db import models


class Orders(models.Model):
    product_name = models.CharField()
    quantity = models.IntegerField()