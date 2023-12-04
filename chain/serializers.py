from rest_framework import serializers
from chain.models import Factory, Product


class FactorySerializer(serializers.ModelSerializer):
    """
    сериализатор для модели завода
    """
    class Meta:
        model = Factory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    сериализатор для модели продукта
    """
    class Meta:
        model = Product
        fields = '__all__'
