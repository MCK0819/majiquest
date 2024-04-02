from django.urls import path, include
from rest_framework import routers
from .views import BbsViewSet

router = routers.DefaultRouter()
router.register(
    '', BbsViewSet
)

urlpatterns = [
    path('', include(router.urls)),
]