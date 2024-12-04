from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from .models import Blog
from .serializers import BlogSerializer, BlogCreateSerializer

# Create your views here.

class BlogsListApi(ListAPIView):
      queryset = Blog.objects.all()
      serializer_class = BlogSerializer
    #   permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class BlogCreateApi(CreateAPIView):
      queryset = Blog.objects.all()
      permission_classes = [IsAuthenticated]
      serializer_class = BlogCreateSerializer

      def perform_create(self, serializer):
            serializer.save(user=self.request.user)
      

#this should be RetrieveUpdateDestroyAPIView after authenticate.
class BlogDetailApi(RetrieveAPIView):
      queryset = Blog.objects.all()
      serializer_class = BlogSerializer
      lookup_field = 'id'