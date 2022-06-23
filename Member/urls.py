from django.contrib import admin
from django.urls import path,include
from requests import post
from .views import UserListView, UserUpdateView,UserUpdatePutView, UserCreateView,UserLoginView, UserTokenRefreshView


urlpatterns = [
    path('member/list',UserListView.as_view(),name='user_list'),
    path('member/login',UserLoginView.as_view(),name='user_login'),
    path('member/refresh',UserTokenRefreshView.as_view(),name='token_refresh'),
    path('member/create',UserCreateView.as_view(),name='user_create'),
    path('member/<int:member_id>/update',UserUpdateView.as_view(), name="user_update"),
    path('member/<int:member_id>/put',UserUpdatePutView.as_view(),name="user_update_put"),
]



