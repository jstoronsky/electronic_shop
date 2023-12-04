from rest_framework import serializers
from retailers.models import Product, Retailer


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'


class RetailerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        exclude = ('debt', )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
