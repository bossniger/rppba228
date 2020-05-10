from django.db import models


class Element(models.Model):

    TYPE_CHOICE = (
        ('Стержни', 'component'),
        ('Формы для карандашей', 'material',),
        ('Формы для ручек', 'material',),
        ('Краска', 'component'),

    )

    depiction = models.CharField(max_length=30)
    type = models.CharField(max_length=50, choices=TYPE_CHOICE)

    def __str__(self):
        return f'{self.type}_{self.character}'