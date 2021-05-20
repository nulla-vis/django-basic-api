
from django import urls
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import article_list,article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    # path('', article_list, name = 'article_list'), 
    # path('', ArticleAPIView.as_view(), name = 'article_list'),
    # path('generic/', GenericAPIView.as_view(), name = 'generic_article_list'),
    # path('generic/<int:id>/', GenericAPIView.as_view(), name = 'generic_article_list'),
    # path('detail/<int:pk>/', article_detail, name = 'article_detail'),
    # path('detail/<int:pk>/', ArticleDetails.as_view(), name = 'article_detail'),
]