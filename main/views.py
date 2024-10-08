from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from django.utils import timezone
from datetime import timedelta

from .filters import ArticleFilter, VideoFilter
from .serializers import *


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'



class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = ArticleFilter
    ordering_fields = '__all__'
    search_fields = ('title', 'intro')

    def get_queryset(self):
        return self.queryset.order_by('-id')

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='publish',
                in_=openapi.IN_QUERY,
                description="Filter articles by publish status",
                type=openapi.TYPE_BOOLEAN,
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TopArticlesListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # def get_queryset(self):
    #     top_news = self.queryset.filter(news_of_the_day=True).order_by('-id')
    #     other_news = self.queryset.filter(news_of_the_day=False).order_by('-views')
    #     return list(top_news) + list(other_news)[:40 - len(top_news)]

    def get_queryset(self):
        last_10_days = timezone.now() - timedelta(days=10)
        top_news = self.queryset.filter(news_of_the_day=True, created_at__gte=last_10_days).order_by('-id')
        other_news = self.queryset.filter(news_of_the_day=False, created_at__gte=last_10_days).order_by('-views')
        return list(top_news) + list(other_news)[:40 - len(top_news)]



class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = VideoFilter
    ordering_fields = '__all__'
    search_fields = ('title', 'intro')


class VideoRetrieveAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class AdListAPIView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdRetrieveAPIView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
