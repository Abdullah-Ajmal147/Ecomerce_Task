from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
  TokenVerifyView
)

from .views import RegisterUserAPIView,UserDetailAPI
from django.urls import path

urlpatterns = [
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
  path('api/user/',RegisterUserAPIView.as_view(), name='user'),
  path('api/user-details/',UserDetailAPI.as_view(), name='user'),

]
