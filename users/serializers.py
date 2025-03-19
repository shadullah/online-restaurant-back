from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = User 
        # fields = "__all__"
        fields = ["id","username", "email", "address", "image", "user_type", "password"]

class LoginSerializer(serializers.Serializer):
    email=serializers.CharField(required=True)
    password=serializers.CharField(required=True)