from django.db import models


class Order(models.Model):
    lol = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lol}'
