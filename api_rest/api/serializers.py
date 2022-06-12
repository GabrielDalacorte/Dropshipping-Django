from django.contrib.auth import get_user_model
from rest_framework import serializers

from api_rest.models import Departments


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'parameter_id', 'departments')
