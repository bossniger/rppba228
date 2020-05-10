from django.db import models
from users.models import User


class MaterialOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()