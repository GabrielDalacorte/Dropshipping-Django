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
