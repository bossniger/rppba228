from django.db import models
from apps.elements.models import Element


class WarehouseMaterial(models.Model):
    element_id = models.ForeignKey(Element, models.CASCADE)
    available_quantity = models.IntegerField(max_length=10)