from rest_framework import serializers
from .models import User

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'user_password']

    def create(self, validated_data):
        user = User.objects.create_user(
            user_name=validated_data['user_name'],
            user_email=validated_data['user_email'],
            user_password=validated_data['user_password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    user_password = serializers.CharField(write_only=True)
