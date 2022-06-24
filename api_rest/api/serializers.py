from django.contrib.auth import get_user_model
from rest_framework import serializers

from api_rest.models import Departments, Product


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('parameter_id', 'departments')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('departament', 'parameter_id', 'url', 'min_price', 'max_price', 'name', 'sales_number', 'description',
                  'rating', 'rating_count')
