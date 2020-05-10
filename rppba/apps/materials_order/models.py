from django.db import models
from apps.warehouse_materials.models import WarehouseMaterial
from users.models import User


class MaterialOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    warehouse_material = models.ForeignKey(WarehouseMaterial, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=10)