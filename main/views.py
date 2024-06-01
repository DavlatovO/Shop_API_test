from django.shortcuts import render
from rest_framework import generics
from .import models
from .serializers import ProductSerializer, CategorySerializer

class ProductAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if False:
            pass
        return models.Product.objects.all()


class ProCategoryAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        if False:
            pass
        return models.Category.objects.all()
