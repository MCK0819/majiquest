from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    ID = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = [
            "ID",
            "nickname",
            "password",
            "password2",
            "created_at",
            "last_login",
            "is_staff",
            "is_active",
            "rank",
            "rating",
        ]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("password2", None)
        return CustomUser.objects.create_user(**validated_data)
