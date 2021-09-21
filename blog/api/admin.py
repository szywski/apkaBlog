from django.contrib import admin
from api.models import BlogArticle, BlogArticleComment, BlogArticleTag
# Register your models here.

admin.site.register(BlogArticle)
admin.site.register(BlogArticleComment)
admin.site.register(BlogArticleTag)

