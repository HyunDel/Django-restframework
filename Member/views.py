from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status

from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserUpdatePutSerializer
from .models import User

# Create your views here.

# 1. serializer 설정
#    - serializer 필드 설정["민감한 정보 표현하지 않기"]
#    - serializer 글로벌 설정
#    - GET, POST 메소드 분기하는 serializer
#    - POST serializer는 4개 필드 사용
# 2. queryset 설정

class UserListView(generics.GenericAPIView):
    """
    사용자 검색

    ---
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method =="POST":
            return UserCreateSerializer
        elif self.request.method =="GET":
            return UserSerializer
    
    def get(self,request):
        serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        serializer = self.get_serializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data,status =status.HTTP_201_CREATED)

class UserUpdateView(generics.UpdateAPIView):
    """
    사용자 업데이트

    ---
    """
    
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_url_kwarg = "member_id"

    @transaction.atomic
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
class UserUpdatePutView(generics.UpdateAPIView):
    """
    사용자 전체 업데이트

    ___
    """
    queryset = User.objects.all()
    serializer_class = UserUpdatePutSerializer
    lookup_url_kwarg = "member_id"

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        queryset = User.objects.filter(id=kwargs["member_id"])
        return self.update(request, *args, **kwargs)
    
    # # 사용자 검색 
    # def get(self,request, **kwargs):
    #     if kwargs.get('id') is None:
    #         Users = User.objects.all()
    #         serializer = UserSerializer(Users, many =True)
    #         return Response(serializer.data,status=200)
    #     else:
    #         user_id= kwargs.get('id')
    #         serializer = UserSerializer(User.objects.get(id=user_id))
    #         return Response(serializer.data,status=200)

    # # 사용자 등록 
    # def post(self,request):
    #     serializer = UserSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data = serializer.data, status = 200)
    #     return Response(data = serializer.data, status = 400)

    # # 사용자 수정 
    # def put(self,request,**kwargs):
    #     if kwargs.get('id') is None:
    #         return Response(status=400)
    #     else:
    #         user_id = kwargs.get('id')
    #         user_object = User.objects.get(id=user_id)

    #         update_user_serializer = UserSerializer(user_object, data=request.data)
    #         if update_user_serializer.is_valid():
    #             update_user_serializer.save()
    #             return Response(update_user_serializer.data,status=200)
    #         else:
    #             return Response(status=400)

    # # 사용자 삭제 
    # def delete(self,request,**kwargs):
    #     if kwargs.get('id') is None:
    #         return Response(status=400)
    #     else:
    #         user_id = kwargs.get('id')
    #         user_object = User.objects.get(id = user_id)
    #         user_object.delete()
    #         return Response(status=200)