from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True)
    
    class Meta:
        model = User
        fields = ["username","phone","email","password","last_login","date_joined"]

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True)

    class Meta:
       model = User
       fields = ["username","phone","email","password"]
