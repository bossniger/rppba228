from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    time_processing = models.DecimalField(max_digits=10, decimal_places=0)


class Material(models.Model):
    material_name = models.CharField(max_length=50)


class Component(models.Model):
    component_name = models.CharField(max_length=50)


# Комплектующие
class component_for_product(models.Model):
    component_id = models.ForeignKey('Component',null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product',null=True, on_delete=models.CASCADE)# не уверен на счет каскадного удаления
    quantity = models.IntegerField()

# Материалы
class material_for_product(models.Model):
    material_id = models.ForeignKey('Material',null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product',null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# Список операций
class Operation(models.Model):
    priorities = [
        ('Высокий','Высокий'),
        ('Средний','Средний'),
        ('Низкий','Низкий'),# градация приоритетов
    ]                       # почему бы и не таким способом?
    operation_name = models.CharField(max_length=50)
    priority = models.CharField(max_length=20, choices=priorities, default='Высокий')


class operation_for_product(models.Model):
    operation_id= models.ForeignKey('Operation', null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    runtime = models.DecimalField(max_digits=3, decimal_places=2)# сделал по твоему примеру
                                                                  # почему не TimeField или DateTime??
# Доступные материалы
class material_available(models.Model):
    material_id = models.ForeignKey('Material', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()