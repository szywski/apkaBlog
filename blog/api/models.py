from django.db import models

# Create your models here.
from django.db import models

class BlogArticle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class Tags(models.Model):
    tagName = models.CharField(max_length=50, blank=True, default='')

class BlogTags(models.Model):
    blogArticlePK = models.ForeignKey(BlogArticle, on_delete=models.CASCADE)
    selectedTag = models.ForeignKey(Tags.tagName,on_delete=models.CASCADE)

