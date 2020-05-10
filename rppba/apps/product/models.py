from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    time_processing = models.DecimalField(max_digits=10, decimal_places=0)


class Material(models.Model):
    material_name = models.CharField(max_length=50)


class Component(models.Model):
    component_name = models.CharField(max_length=50)


# Комплектующие
class ComponentForProduct(models.Model):
    component_id = models.ManyToManyField(Component)
    product_id = models.ManyToManyField(Product)
    quantity = models.IntegerField()

# Материалы
class MaterialForProduct(models.Model):
    material_id = models.ManyToManyField(Material )
    product_id = models.ManyToManyField(Product)
    quantity = models.IntegerField()

# Список операций
class Operation(models.Model):
    priorities = [
        ('High','High'),
        ('Mid','Mid'),
        ('Low','Low'),# градация приоритетов
    ]                       # почему бы и не таким способом?
    operation_name = models.CharField(max_length=50)
    priority = models.CharField(max_length=20, choices=priorities, default='Высокий')

class OperationForProduct(models.Model):
    operation_id= models.ManyToManyField(Operation)
    product_id = models.ManyToManyField(Product)
    runtime = models.DecimalField(max_digits=3, decimal_places=2)# сделал по твоему примеру
                                                                  # почему не TimeField или DateTime??
# Доступные материалы
class MaterialAvailable(models.Model):
    material_id = models.ForeignKey('Material', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()