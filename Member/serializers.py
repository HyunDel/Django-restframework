from rest_framework import serializers
from .models import User

# UserSerializer
# Return data
# username = tpdnrzz[01041778514]
# date_joined = "yy-mm-dd hh" 

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

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["phone","email"]
class UserUpdatePutSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
