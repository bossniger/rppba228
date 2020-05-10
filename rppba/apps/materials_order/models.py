from django.db import models
from apps.warehouse_materials.models import WarehouseMaterials
from users.models import User


class MaterialOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    warehouse_material = models.ForeignKey(WarehouseMaterials, on_delete=models.CASCADE)
    quantity = models.IntegerField()