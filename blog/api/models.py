from django.db import models

# Create your models here.
from django.db import models


class Tags(models.Model):
    tagName = models.CharField(max_length=50, blank=True, default='')

class BlogArticle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='blogArticles', on_delete=models.CASCADE)
    tagsSelected = models.ForeignKey(Tags,on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['created']



