from rest_framework import serializers
from businessmen.models import Businessman, Product


class BusinessmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessman
        fields = '__all__'


class BusinessmanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessman
        exclude = ('debt', )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
