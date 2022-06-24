from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api_rest.api.serializers import DepartmentsSerializer, ProductSerializer
from api_rest.models import Departments, Product


class DepartmentsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer