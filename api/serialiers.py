from rest_framework import serializers
from .models import *


class CategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class BookSelializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')


class ProductSelializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
