from django.urls import path

from . import views

urlpatterns = [
    path('blog', views.BlogsListApi.as_view())
]
