from django.db import models


class OperationsList(models.Model):

    TYPE_CHOICE = (
        ('1', '1'),
        ('2', '2',),
        ('3', '3',),
        ('4', '4',),
    )

    name = models.CharField(max_length=30)
    priority = models.CharField(max_length=50, choices=TYPE_CHOICE)

    def __str__(self):
        return f'{self.name}'


