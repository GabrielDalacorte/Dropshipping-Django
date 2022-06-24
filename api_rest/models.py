from django.db import models


# Create your models here.


class Departments(models.Model):
    departments_choices = [
        ('Eletronicos', 'Eletronicos'),
        ('Acessorios', 'Acessorios'),
    ]
    parameter_id = models.IntegerField(primary_key=True)
    departments = models.CharField(max_length=100, choices=departments_choices)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return f'{self.parameter_id} - {self.departments}'


class Product(models.Model):
    departament = models.ForeignKey(Departments, on_delete=models.CASCADE)
    parameter_id = models.IntegerField(primary_key=True)
    url = models.URLField(max_length=300, blank=False, null=False)
    min_price = models.FloatField(blank=True, null=True)
    max_price = models.FloatField(blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    sales_number = models.IntegerField(blank=False, null=False)
    description = models.TextField(max_length=400, blank=True, null=True)
    rating = models.FloatField(blank=False, null=False, default=0.0)
    rating_count = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.parameter_id} - {self.name} - {self.max_price}'
