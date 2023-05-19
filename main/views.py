from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer