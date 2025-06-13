from rest_framework import serializers
from .models import User, Post, Follows


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'role']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'user_id']


class FollowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follows
        fields = ['following_user_id', 'followed_user_id']
