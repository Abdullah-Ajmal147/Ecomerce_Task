from .models import Category, Brand, City, State, Country, Products
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Products
    fields = '__all__'
