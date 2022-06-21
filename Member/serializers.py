from itertools import count
from time import strftime
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from datetime import datetime
from .models import User

# 직렬화 할때 data overrding # 완료 
# a = 1
# database 생성
# a = 2
# 오버라이딩

# 직렬화 할때 # 완료 
# 데이터를 업데이트 하는 순간
# 어떻게 값들을 넣어줄 건지
# 정의하는 부분이 있음

# 값 체크 # 완료
# 실제로 값들이 잘 들어갔는지 체크하는 부분을 직접 핸들링

# 모델 직렬화 # 완료 
# 필드 읽기만 하는 옵션을 넣어줄 수 있음 확인해보기 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    username =serializers.SerializerMethodField()
    date_joined = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ["username","date_joined","password","phone"]
        read_only_fields = ["password"]

    def get_username(self,instance):
        instance.username = f"{instance.username}[{instance.phone}]"
        return instance.username

    def get_date_joined(self,instance):
        return instance.date_joined.strftime('%Y-%m-%d %H시')

    def to_representation(self, instance):
        return super().to_representation(instance)
        

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
       model = User
       fields = ["username","phone","email","password"]
       read_only_fields = ["password"]

    def join(self,validated_data):
        print(1)
        user = User(username=validated_data.get("username"),
        phone = validated_data.get("phone"),
        email = validated_data.get("email"),
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    # # object 단위로 사용할 때 
    # def validate(self, attrs):
    #     # if len(attrs["phone"]) < 11:
    #     raise ValidationError("test")
    #     return attrs

    # 필드 단위로 사용할 때 
    def validate_phone(self, value):
        if len(value) < 11:
            raise ValidationError("asdasdasd")
        return value


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["phone","email"]

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email',instance.email)
        instance.phone = "1231231"
        instance.save()

        return instance
        


class UserUpdatePutSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
