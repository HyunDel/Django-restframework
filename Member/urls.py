from django.contrib import admin
from django.urls import path,include
from requests import post
from .views import UserListView, UserUpdateView
urlpatterns = [
    path('',UserListView.as_view(),name='user_list'),
    path('update/<int:id>/',UserUpdateView.as_view(), name="user_update"),
]



