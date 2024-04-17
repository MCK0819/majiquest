from django.urls import path

from .views import KakaoCallBackView, KakaoView, RegisterView

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("kakao_login", KakaoView.as_view()),
    path("kakao/oauth", KakaoCallBackView.as_view()),
]
