from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('blogarticles/', views.BlogArticleList.as_view()),
    path('blogarticles/<int:pk>', views.BlogArticleDetail.as_view()),
    path('blogarticlecomments/',views.BlogArticleCommentList.as_view()),
    path('blogarticlecomments/<int:pk>',views.BlogArticleCommentDetail.as_view()),
    path('blogarticletag/',views.BlogArticleTagList.as_view()),
    path('blogarticletag/<int:pk>',views.BlogArticleTagList.as_view()),
    path('blogcategories/',views.BlogArticleCategoryList.as_view()),
    path('blogcategories/<int:pk>',views.BlogArticleCategoryDetail.as_view()),



]

# urlpatterns = format_suffix_patterns(urlpatterns)