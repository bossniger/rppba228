from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
# Create your models here.


class User(AbstractUser):

    ROLE_CHOICE = (
        ('dispatcher', 'dispatcher'),
        ('technologist', 'Technologist'),
        ('Assembly workshop master', 'assembly_workshop_master'),
        ('Workshop master', 'workshop_master'),)

    username = models.CharField(max_length=35, default=None, db_column='username', unique=True)
    first_name = models.CharField(max_length=35, blank=True,  db_column='first_name')
    last_name = models.CharField(max_length=35, blank=True,  db_column='last_name')
    role = models.CharField(max_length=100, choices=ROLE_CHOICE, default='')
    position = models.CharField(max_length=100, blank=True)

    date_joined = None
    last_login = None
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.id} {self.role} {self.username}'
