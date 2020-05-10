from django.db import models
from apps.elements.models import Elements


class WarehouseMaterials(models.Model):
    element_id = models.ForeignKey(Elements,models.CASCADE)
    available_quantity = models.IntegerField()