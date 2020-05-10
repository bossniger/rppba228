from django.db import models

from apps.products.models import Product
from users.models import User


class ProductionOrder(models.Model):

    STATUS_CHOICE = (
        ('создано', 'created'),
        ('запланировано', 'planed',),
        ('Процесс начат', 'process_finished'),
        ('Процесс завершён', 'process_finished'),
        ('Завершение заказа', 'finished'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(max_length=30)
    lead_time_production = models.CharField(max_length=30)
    production_start = models.DateTimeField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='created')
    master = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f' аказ на {self.product.name}'