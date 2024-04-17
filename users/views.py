import environ
import requests
from django.shortcuts import HttpResponse, redirect
from rest_framework import generics

from .models import CustomUser
from .serializers import CustomUserSerializer

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class KakaoView(generics.GenericAPIView):
    def get(self, request):
        kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        client_id = env("CLIENT_ID")
        redirect_uri = "http://127.0.0.1:8000/users/kakao/oauth"

        print(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")
        return redirect(
            f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}"
        )


class KakaoCallBackView(generics.GenericAPIView):
    print("눌림")

    def get(self, request):
        data = {
            "grant_type": "authorization_code",
            "client_id": env("CLIENT_ID"),
            "redirect_uri": "http://127.0.0.1:8000/users/kakao/oauth",
            "code": request.GET["code"],
        }

        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        access_token = requests.post(kakao_token_api, data=data).json()["access_token"]

        return HttpResponse(access_token)
