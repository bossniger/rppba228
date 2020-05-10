from django.db import models


class Product(models.Model):

    TYPE_CHOICE = (
        ('pen', 'pen'),
        ('pencil', 'pencil',),
    )

    model_name = models.CharField(max_length=30)
    type = models.CharField(max_length=50, choices=TYPE_CHOICE)
    product_time_production = models.CharField(max_length=100, default='0')

    def __str__(self):
        return f'{self.type} {self.model_name}'