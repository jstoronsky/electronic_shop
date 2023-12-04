from rest_framework import viewsets
from businessmen.models import Businessman, Product
from businessmen.serializers import BusinessmanSerializer, ProductSerializer, BusinessmanUpdateSerializer
from chain.permissions import IsActive
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework
# Create your views here.


class BusinessmanViewSets(viewsets.ModelViewSet):
    queryset = Businessman.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['country']

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return BusinessmanUpdateSerializer
        else:
            return BusinessmanSerializer


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]
