from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from .models import *


class PostAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['GET'], detail=True)
    def post_comments(self, request, pk):
        comments = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def post_comments_to_third(self, request, pk):
        comments = Comment.objects.filter(post=pk, level__lte=3)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def post_comments_from_third(self, request, pk):
        comments = Comment.objects.filter(post=pk, level__gte=3)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer

    @action(methods=['GET'], detail=False)
    def comments_to_third(self, request):
        comments = Comment.objects.filter(level__lte=3)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def comments_from_third(self, request):
        comments = Comment.objects.filter(level__gte=3)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
