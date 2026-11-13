from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerailizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username","email","password","password2"]

    def validate(self,data):
        if data["password"] != data["password2"]:
            return serializers.ValidationError("Passwords do not match")
        
        if User.objects.filter(username=data["username"]).exists():
            return serializers.ValidationError("Username already exists")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        return User.objects.create_user(**validated_data)


class Userserailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]

