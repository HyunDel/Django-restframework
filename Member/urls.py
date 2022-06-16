from django.contrib import admin
from django.urls import path,include
from requests import post
from .views import UserListView, UserUpdateView,UserUpdatePutView
urlpatterns = [
    path('member',UserListView.as_view(),name='user_list'),
    path('member/<int:member_id>/update',UserUpdateView.as_view(), name="user_update"),
    path('member/<int:member_id>/put',UserUpdatePutView.as_view(),name="user_update_put")
]



