from rest_framework import generics

from .models import CustomUser
from .serializers import CustomUserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
