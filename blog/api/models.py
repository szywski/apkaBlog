from django.db import models

# Create your models here.
from django.db import models




class BlogArticle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='blogArticles', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']
        managed = True


class BlogArticleTag(models.Model):
    tagName = models.CharField(max_length=50, blank=True, default='')
    blogArticle = models.ForeignKey('BlogArticle', related_name='blogarticletag',on_delete=models.CASCADE)


class BlogArticleComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='blogarticlecomments',on_delete=models.CASCADE)
    blogArticle = models.ForeignKey('BlogArticle',related_name='blogarticlecomments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class BlogArticleCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, default="")
    owner = models.ForeignKey('auth.User', related_name='blogarticlecategory', on_delete=models.CASCADE)
    blogArticle = models.ManyToManyField('BlogArticle', related_name='blogarticlecategory', blank=True)

    class Meta:
        verbose_name_plural='Categories'
        db_table = 'blogarticlecategory'
        managed=True



