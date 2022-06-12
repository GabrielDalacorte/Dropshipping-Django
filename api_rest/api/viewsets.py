from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api_rest.api.serializers import DepartmentsSerializer
from api_rest.models import Departments


class DepartmentsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
