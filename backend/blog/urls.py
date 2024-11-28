from django.urls import path

from . import views

urlpatterns = [
    path('blog', views.BlogsListApi.as_view()),
    path('blog/create', views.BlogCreateApi.as_view()),
    # path('blog/delete'),
    path('blog/<int:id>', views.BlogDetailApi.as_view())
]
