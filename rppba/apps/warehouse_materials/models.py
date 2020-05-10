from django.db import models
from apps.elements.models import Elements


class WarehouseMaterials(models.Model):
    element_id = models.ForeignKey(Elements)
    available_quantity = models.IntegerField()