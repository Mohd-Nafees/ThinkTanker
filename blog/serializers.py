from rest_framework import serializers
from blog.models import User, Blog, Like
from rest_framework.exceptions import ValidationError


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        user = User.objects.filter(email=attrs['email'], password=attrs['password']).first()

        if not user:
            raise ValidationError("The user email or password not valid")

        return validated_data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'about', 'created')


class BlogSerializer(serializers.ModelSerializer):
    count_like = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'user', 'title', 'description', 'content', 'count_like', 'created')

    def get_count_like(self, obj):
        count = Like.objects.filter(blog=obj).count()
        return count


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('id', 'user', 'blog', 'created')
