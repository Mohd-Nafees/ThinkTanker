from django.urls import path, include
from rest_framework import routers
from blog.views import UserViewSet, BlogViewSet, LikeViewSet

router = routers.SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('blog', BlogViewSet, basename='blog')
router.register('like', LikeViewSet, basename='like')

app_name = 'blog'

urlpatterns = [
    path('', include(router.urls)),
]