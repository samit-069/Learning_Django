from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment

#simple user serializer to display author details
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

#comment serializer
class CommentSerializer(serializers.ModelSerializer):
    #read-only nested representation of author details

    author = UserSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']

#Post serializer
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    #Include nested comment directly inside the post response
    comments = CommentSerializer(many = True, read_only = True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'comments', 'created_at', 'updated_at']

#Registration serializer
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data.get('email', ''),
            password= validated_data['password']
        )
        return user