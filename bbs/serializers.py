from rest_framework import serializers
from bbs.models import Board

class BbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'content', 'category', 'author']