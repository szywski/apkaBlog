from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import BlogArticle, BlogArticleComment, BlogArticleTag




class BlogArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    blogarticlecomments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    blogarticletag = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = BlogArticle
        fields = ['id','title','body','owner', 'blogarticlecomments','blogarticletag']

class UserSerializer(serializers.ModelSerializer):
    blogArticles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    blogarticlecomments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name']


class BlogArticleCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BlogArticleComment
        fields = ['id','body','owner','blogArticle']


class BlogArticleTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogArticleTag
        fields= ['tagName','blogArticle']