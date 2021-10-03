"""blog URL Configuration

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
from django.urls import path, include
from rest_framework import permissions
from rest_framework.swagger.views import get_swagger_view

from drf_yasg import openapi
schema_view = get_swagger_view(
    openapi.Info(
        title="api",
        default_version='v1',
        description="blog article api",

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('',schema_view),
    path('admin/', admin.site.urls),
    path('blogapi', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
