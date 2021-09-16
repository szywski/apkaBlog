from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import BlogArticle




class BlogArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BlogArticle
        fields = ['id','title','body','owner','tagsSelected']

class UserSerializer(serializers.ModelSerializer):
    blogArticles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name']