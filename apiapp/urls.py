from apiapp import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register('songapi', views.SongViewSet, basename='song')
router.register('singerapi', views.SingerViewSet, basename='singer')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
