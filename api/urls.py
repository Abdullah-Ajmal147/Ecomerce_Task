from . import views
from django.urls import path
from .views import CategoryView, BrandView, ProductsView,ProductsViewDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryView, basename='category')
# router.register(r'product',ProductsView.as_view() , basename='product')
router.register(r'brand', BrandView, basename='brand')



urlpatterns = [
  # path('api/category/', views.CategoryView.as_view(), name='category'),
  path('api/city/', views.CityView.as_view(), name='city'),
  # path('api/brand/', views.BrandView.as_view(), name='brand'),
  path('api/country/',views.CountryView.as_view(), name='country'),
  path('api/state/',views.StateView.as_view(), name='state'),
  path('api/product/',ProductsView.as_view() , name='product'),
  path('api/product/<int:pk>/',ProductsViewDetail.as_view() , name='product')

]+ router.urls

