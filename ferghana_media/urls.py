from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authentication import BasicAuthentication
from django.conf.urls.i18n import set_language

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.i18n import i18n_patterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from main.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Fergana Media API",
        default_version='v1',
        description="Fergana Media",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cbekoder@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],
    authentication_classes=[BasicAuthentication],
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

    path('', schema_view.with_ui('swagger', cache_timeout=0)),

    path('set_language/', set_language, name='set_language'),

    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-retrieve'),
    path('articles/', ArticleListAPIView.as_view(), name='article-list'),
    path('articles-top/', TopArticlesListAPIView.as_view(), name='article-top-list'),
    path('articles/<int:pk>/', ArticleRetrieveAPIView.as_view(), name='article-retrieve'),
    path('videos/', VideoListAPIView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoRetrieveAPIView.as_view(), name='video-retrieve'),
    path('ads/', AdListAPIView.as_view(), name='ad-list'),
    path('ads/<int:pk>/', AdRetrieveAPIView.as_view(), name='ad-retrieve'),
    path('staff/', StaffListAPIView.as_view(), name='staff-list'),
    path('staff/photos/', StaffPhotoListAPIView.as_view(), name='staff-photo-list'),
    path('credentials/', CredentialsApiView.as_view(), name='credentials-list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]
