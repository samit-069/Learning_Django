from rest_framework import viewsets
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer, RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # Explicitly pass the logged-in user to the serializer on save
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer