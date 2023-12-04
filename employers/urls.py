from employers.apps import EmployersConfig
from django.urls import path
from employers.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserMeAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = EmployersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', UserListAPIView.as_view(), name='users_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='users_detail'),
    path('me/', UserMeAPIView.as_view(), name='me')
]
