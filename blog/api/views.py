from rest_framework import generics
from api import serializers
from api.models import BlogArticle, BlogArticleComment,BlogArticleTag, BlogArticleCategory
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


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
    serializer_class = serializers.BlogArticleCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BlogArticleTagList(generics.ListCreateAPIView):
    queryset = BlogArticleTag.objects.all()
    serializer_class = serializers.BlogArticleTagSerializer
    filterset_fileds = ('blogArticle',)

    def perform_create(self, serializer):
        serializer.save()

class BlogArticleTagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogArticleTag.objects.all()
    serializer_class = serializers.BlogArticleTagSerializer


class BlogArticleCategoryList(generics.ListCreateAPIView):
    queryset = BlogArticleCategory.objects.all()
    serializer_class = serializers.BlogArticleCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BlogArticleCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogArticleCategory.objects.all()
    serializer_class = serializers.BlogArticleCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_user_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



