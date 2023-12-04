from rest_framework import viewsets
from retailers.models import Retailer, Product
from retailers.serializers import RetailerSerializer, ProductSerializer, RetailerUpdateSerializer
from chain.permissions import IsActive
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RetailerViewSets(viewsets.ModelViewSet):
    """
    Вьюсеты для ритейлера, настроена фильтрация по стране
    """
    queryset = Retailer.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['country']

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return RetailerUpdateSerializer
        else:
            return RetailerSerializer


class ProductViewSets(viewsets.ModelViewSet):
    """
    Вьюсеты для продукта
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]
