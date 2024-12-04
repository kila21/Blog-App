from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from . import views

urlpatterns = [
    # host:/api/blog .........
    path('blog', views.BlogsListApi.as_view()),
    path('blog/create', views.BlogCreateApi.as_view()),
    # path('blog/delete'),
    path('blog/<int:id>', views.BlogDetailApi.as_view()),

    # host:/api/token....
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
