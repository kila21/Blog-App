from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Blog
from .serializers import BlogSerializer, BlogCreateSerializer

# Create your views here.

class BlogsListApi(ListAPIView):
      queryset = Blog.objects.all()
      serializer_class = BlogSerializer
    #   permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class BlogCreateApi(CreateAPIView):
      queryset = Blog.objects.all()
      serializer_class = BlogCreateSerializer
      