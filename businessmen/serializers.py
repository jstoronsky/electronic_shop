from rest_framework import serializers
from businessmen.models import Businessman, Product


class BusinessmanSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели предпринимателя
    """
    class Meta:
        model = Businessman
        fields = '__all__'


class BusinessmanUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления модели предпринимателя. Исключено поле долга, чтобы его нельзя было
    поменять через API
    """
    class Meta:
        model = Businessman
        exclude = ('debt', )


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели продукта
    """
    class Meta:
        model = Product
        fields = '__all__'
        ref_name = 'product_businessman'
