from django.urls import path
from api_rest.views import home

urlpatterns = [
    path('', home),
]
