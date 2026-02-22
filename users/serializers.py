from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "user_name", "user_email", "user_password", "created_at"]
        extra_kwargs = {
            "user_password": {"write_only": True}
        }

    def create(self, validated_data):
        validated_data["user_password"] = make_password(
            validated_data["user_password"]
        )
        return super().create(validated_data)