from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICE = (
        ('technologist', 'technologist'),
        ('dispatcher', 'dispatcher',),
        ('master_paint_workshop', 'master of the paint shop'),
        ('master_paint_workshop', 'master of the paint shop'),
        ('master_assembly_workshop', 'assembly shop master'),
        ('master_packing_workshop', 'packing shop master', ),
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            'unique': 'This email is already in use in the Monfluence system.'
                      ' Please login or use a different email',
        },
    )
    name = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=25, choices=ROLE_CHOICE)
