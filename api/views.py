from django.shortcuts import render

# Create your views here.
from rest_framework import generics, response, viewsets, status
from rest_framework.permissions import IsAuthenticated

from api.models import Category, Brand, City, State, Country, Products
from api.serializers import CitySerializer, CountrySerializer, CategorySerializer, StateSerializer, BrandSerializer, \
  ProductsSerializer


class CategoryView(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAuthenticated]


class BrandView(viewsets.ModelViewSet):
  queryset = Brand.objects.all()
  serializer_class = BrandSerializer
  permission_classes = []


class CityView(generics.GenericAPIView):
  queryset = City.objects.all()
  serializer_class = CitySerializer
  permission_classes = []

  def get(self, request, *args, **kwargs):
    city_data = self.queryset.all()
    serialized = self.get_serializer(city_data, many=True)
    return response.Response(serialized.data)


class StateView(generics.GenericAPIView):
  queryset = State.objects.all()
  serializer_class = StateSerializer
  permission_classes = []

  def get(self, request, *args, **kwargs):
    state_data = self.queryset.all()
    serialized = self.get_serializer(state_data, many=True)
    return response.Response(serialized.data)


class CountryView(generics.GenericAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer
  permission_classes = []

  def get(self, request, *args, **kwargs):
    country_data = self.queryset.all()
    serialized = self.get_serializer(country_data, many=True)
    return response.Response(serialized.data)


class CountryView(generics.GenericAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer
  permission_classes = []

  def get(self, request, *args, **kwargs):
    country_data = self.queryset.all()
    serialized = self.get_serializer(country_data, many=True)
    return response.Response(serialized.data)


class ProductsView(generics.GenericAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductsSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request, *args, **kwargs):
    products = self.queryset.filter(user=request.user.id)
    serialized = self.get_serializer(products, many=True)
    return response.Response(serialized.data)

  def post(self, request, *args, **kwargs):
    if request.user.id == request.data['user']:
      serialized = self.get_serializer(data=request.data)
      if serialized.is_valid():
        serialized.save()
        return response.Response(serialized.data)
      return response.Response(serialized.errors)
    return response.Response("Dose Not Permission to add Poduct against other user.")


class ProductsViewDetail(generics.GenericAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductsSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request, *args, **kwargs):
    if kwargs.get("pk"):
      product = Products.objects.get(id=kwargs.get("pk"))
      serialized = self.get_serializer(product)
    return response.Response(serialized.data)

  def put(self, request, *args, **kwargs):
    if kwargs.get("pk"):
      product = Products.objects.get(id=kwargs.get("pk"))
      serialized = self.get_serializer(product, data=request.data)
      if serialized.is_valid():
        serialized.save()
        return response.Response(serialized.data)
      return response.Response(serialized.errors)
    return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

  def delete(self, request, *args, **kwargs):
    if kwargs.get("pk"):
      product = Products.objects.get(id=kwargs.get("pk"))
      product.delete()
      return response.Response(status=status.HTTP_204_NO_CONTENT)
    return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
