from rest_framework import generics
from django.shortcuts import render
from api import serializers
from api.models import BlogArticle

from django.contrib.auth.models import User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class BlogArticleList(generics.ListCreateAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = serializers.BlogArticleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BlogArticleDetail(generics.RetrieveUpdateAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = serializers.BlogArticleSerializer


# Create your views here.
