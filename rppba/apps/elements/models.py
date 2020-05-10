from django.db import models


class Elements(models.Model):

    TYPE_CHOICE = (
        ('component', 'component'),
        ('material', 'material',),
    )

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=50, choices=TYPE_CHOICE)

    def __str__(self):
        return f'{self.type}_{self.name}'