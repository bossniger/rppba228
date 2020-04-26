from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICE = (
        ('technologist', 'technologist'),
        ('dispatcher', 'dispatcher'),
        ('master', 'master'),
        ('packaging_master', 'packaging_master'),
    )

    username = models.CharField(max_length='100', unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICE)
    position = models.CharField(max_length=50)

    def set_password(self, raw_password):
        super().set_password(raw_password)

