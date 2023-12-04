from rest_framework import serializers
from retailers.models import Product, Retailer


class RetailerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ритейлера
    """
    class Meta:
        model = Retailer
        fields = '__all__'


class RetailerUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления модели ритейлера. Исключено поле долга, чтобы его нельзя было
    поменять через API
    """
    class Meta:
        model = Retailer
        exclude = ('debt', )


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели продукта
    """
    class Meta:
        model = Product
        fields = '__all__'
