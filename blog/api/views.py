from rest_framework import generics
from django.shortcuts import render
from api import serializers
from api.models import BlogArticle, BlogArticleComment,BlogArticleTag
from rest_framework import permissions

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BlogArticleDetail(generics.RetrieveUpdateAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = serializers.BlogArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BlogArticleCommentList(generics.ListCreateAPIView):
    queryset = BlogArticleComment.objects.all()
    serializer_class = serializers.BlogArticleCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BlogArticleCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogArticleComment.objects.all()
    serializer_class = serializers.BlogArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BlogArticleTagList(generics.ListCreateAPIView):
    queryset = BlogArticleTag.objects.all()
    serializer_class = serializers.BlogArticleTagSerializer
    def perform_create(self, serializer):
        serializer.save()

class BlogArticleTagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogArticleTag.objects.all()
    serializer_class = serializers.BlogArticleTagSerializer
# Create your views here.
