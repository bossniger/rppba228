from django.db import models


class Element(models.Model):

    TYPE_CHOICE = (
        ('rods', 'Стержни'),
        ('pencil shapes', 'Формы для карандашей'),
        ('pen shapes', 'Формы для ручек'),
        ('paint', 'Краска'),

    )

    depiction = models.CharField(max_length=30)
    type = models.CharField(max_length=50, choices=TYPE_CHOICE)

    def __str__(self):
        return f'{self.type}_{self.depiction}'