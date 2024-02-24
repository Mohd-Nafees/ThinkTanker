from rest_framework import viewsets, permissions, mixins
from blog.models import User, Blog, Like
from blog.serializers import BlogSerializer, UserSerializer, LikeSerializer, LoginSerializer
# from utils.permissions import IsAPIKEYAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    @action(methods=['post'], detail=False, url_name='login', url_path='login')
    def login(self, request, *args, **kwargs):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        return Response(data)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]


