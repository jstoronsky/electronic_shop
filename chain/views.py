from rest_framework import viewsets
from chain.models import Factory, Product
from chain.serializers import FactorySerializer, ProductSerializer
from chain.permissions import IsActive
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# Create your views here.


class FactoryViewSets(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['country']


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]
