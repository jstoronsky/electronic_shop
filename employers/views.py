from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import generics
from employers.serializers import UserSerializer
from employers.models import Employee
from employers.permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт для регистрации пользователя
    """
    permission_classes = [IsAuthenticated, IsSuperUser]
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = UserSerializer


class UserMeAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            obj = Employee.objects.get(pk=self.request.user.id)
            return obj
        except ObjectDoesNotExist:
            raise Http404
