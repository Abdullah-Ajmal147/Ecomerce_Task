from rest_framework import generics, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from .models import User
from .serializer import UserSerializer, RegisterSerializer


# Create your views here.


# class UserView(generics.GenericAPIView):
#   serializer_class = UserSerializer
#
#   queryset = User.objects.all()
#
#   def post(self, request, *args, **kwargs):
#     serialized = self.get_serializer(data=request.data)
#     if serialized.is_valid():
#       serialized.save()
#       return response.Response(serialized.data)
#     return response.Response(serialized.errors)

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, *args, **kwargs):
    try:
      user = User.objects.get(id=request.user.id)
      serializer = UserSerializer(user)
      return response.Response(serializer.data)
    except Exception as e:
      return response.Response("user dose not exist")


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
