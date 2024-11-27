from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Blog
from .serializers import BlogSerializer

# Create your views here.

class BlogsListApi(ListAPIView):
      queryset = Blog.objects.all()
      serializer_class = BlogSerializer
      permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    #   return Response(serializer.data, status=status.HTTP_200_OK) 