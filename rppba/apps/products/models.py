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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        operations = self.operations_ref.all()
        count = 0
        for operation in operations:
            count += operation.time_processing

        self.product_time_production = str(count)

        super().save()