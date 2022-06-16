"""BaseUser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("Member.urls")),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/verify/',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/token/refresh/',TokenVerifyView.as_view(),name='token_verify'),

]


schema_view = get_schema_view(
    openapi.Info(
        title = "테스트 API",
        default_version="v",
        description="테스트 환경",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="pshyun1331@gmail.com"), # 부가정보
        license=openapi.License(name="mit"),     # 부가정보
        
    ),
    public = True,

)

urlpatterns += [
        path(
            "swagger<str:format>",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]

