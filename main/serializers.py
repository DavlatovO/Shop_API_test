from rest_framework import serializers

from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from .models import Product, Category, Review

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    body = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.body = validated_data.get('body', instance.body)
        instance.quantity = validated_data.get('quantity', instance.quantity)     
        instance.save()
        return instance
    
class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
