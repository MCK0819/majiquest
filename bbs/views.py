from rest_framework import viewsets
from .serializers import BbsSerializer
from .models import Board

class BbsViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BbsSerializer